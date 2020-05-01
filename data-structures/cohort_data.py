"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()

    # get all the school profile data based on the filename
    school_data = all_data(filename)

    # go through each profile in the school data
    for profile in school_data:
      # retrieve the house information from the profile
      house = profile[1]

      # only add the house to the set of houses if there is a house
      if not house == '':
        houses.add(house)

    # return the set of all house names
    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    # get all the school profile data based on the filename
    school_data = all_data(filename)

    for profile in school_data:
      # get the individual profile's cohort
      profile_cohort = profile[3]

      if profile_cohort == 'I' or profile_cohort == 'G':
        # don't add to the students list if the profile belongs to a prof or ghost
        # and move on to the next profile
        continue

      # any remaining profiles from hereon should be a student
      else:
        if (cohort == 'All') or (profile_cohort == cohort):
          # if cohort is 'All', no cohort filtering
          # or if the profile_cohort matches the cohort requested
          # then get the student's name and add it to the list of students
          profile_name = profile[0]

          students.append(profile_name)

    # return a sorted list of the students for the cohort filter requested
    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # get all the school data from the file
    school_data = all_data(filename)

    # sort all the profiles based on their houses
    for profile in school_data:
      profile_name = profile[0]
      profile_house = profile[1]

      if profile_house == "":
        # if profile's house is empty, must be either instructor or ghost
        profile_cohort = profile[3]

        # cohort indicates is instructor, so add to instructors list
        if profile_cohort == "I":
          instructors.append(profile_name)
        elif profile_cohort == "G":
          # otherwise it's a ghost, so add to the ghosts
          ghosts.append(profile_name)

      elif profile_house == "Dumbledore's Army":
        dumbledores_army.append(profile_name)

      elif profile_house == "Gryffindor":
        gryffindor.append(profile_name)

      elif profile_house == "Hufflepuff":
        hufflepuff.append(profile_name)

      elif profile_house == "Ravenclaw":
        ravenclaw.append(profile_name)

      elif profile_house == "Slytherin":
        slytherin.append(profile_name)

    # sort all the individual house lists
    # and put them into one list of house lists
    houses = [sorted(dumbledores_army), sorted(gryffindor),
              sorted(hufflepuff), sorted(ravenclaw),
              sorted(slytherin), sorted(ghosts), sorted(instructors)]

    return houses


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # retrieve and convert the data given by the data file into something parsable
    file = open(filename)
    for line in file:
      line = line.rstrip()
      profile_token = line.split('|')

      # parse the data to their individual profile elements
      first_name = profile_token[0]
      last_name = profile_token[1]
      house = profile_token[2]
      advisor = profile_token[3]
      cohort = profile_token[4]

      full_name = f"{first_name} {last_name}"

      # collect them together into a profile tuple
      profile = (full_name, house, advisor, cohort)
      # add the single profile into the list of all data
      all_data.append(profile)

    # return the list of all the profile data
    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
