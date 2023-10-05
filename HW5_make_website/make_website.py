def read_file(path):
    """
    Opens and reads a file.

    Args:
        path (str): file path
    Returns:
        list: all lines in txt file
    """
    with open(path, "r") as f:
        lines = f.readlines()
    return lines


def handle_name(name):
    """
    1. Checks if the first latter in 'name' is uppercase.
    2. Removes leading or trailing whitespace.

    Args:
        name (str): the name of resume
    Returns:
        str: "Invalid Name" if 'name' is invalid, otherwise revised name
    """
    name_strip = name.strip()
    if name_strip[0].isupper():
        return name_strip
    return "Invalid Name"


def detect_email(line):
    """
    Detects if the part of 'line' is an email in resume.

    Args:
        line (str): single line of information in resume
    Returns:
        bool: True if 'line' is email, otherwise False
    """
    return "@" in line


def handle_email(email):
    """
    1. Checks if 'email' is a valid email.
    2. Removes leading or trailing whitespace.

    Args:
        email (str): email
    Returns:
        str: empty string if 'email' is invalid, otherwise revised email
    """
    # removes leading or trailing whitespace
    email_strip = email.strip()

    # checks if the last four characters of the email are either ".com" or ".edu"
    if email_strip[-4:] not in (".com", ".edu"):
        return ""
    # checks if the first latter after the "@" is lowercase
    if not email_strip[email_strip.index("@") + 1].islower():
        return ""
    # checks if the email does not contain any digits or numbers
    if any(e.isdigit() for e in email_strip):
        return ""
    return email_strip


def detect_courses(line):
    """
    Detects if the part of 'line' is courses in resume.

    Args:
        line (str): single line of information in resume
    Returns:
        bool: True if 'line' is courses, otherwise False
    """
    return "Courses" in line


def handle_courses(courses):
    """
    1. Finds the actual course names from 'line'.
    2. Removes leading or trailing whitespace.

    Args:
        courses (str): single line of courses
            - format: Courses --punctuations-- course 1, course 2, ...
    Returns:
        list: all the actual courses
    """
    # removes "Courses" in the courses string
    courses_new = courses.strip()[7:]
    start_idx = 0

    # checks the index of the first actual course
    for idx, c in enumerate(courses_new):
        if c.isalpha():
            start_idx = idx
            break
    # makes actual courses list
    courses_actual = courses_new[start_idx:].split(",")

    # removes leading or trailing whitespace in each course
    courses_strip = [course.strip() for course in courses_actual]
    return courses_strip


def detect_projects_start(line):
    """
    Detects 'line' is the start of the projects part in resume.

    Args:
        line (str): single line of information in resume
    Returns:
        bool: True if 'line' is the start of the project, otherwise False
    """
    return "Projects" in line


def detect_projects_end(line):
    """
    Detects 'line' is the end of the projects part in resume.

    Args:
        line (str): single line of information in resume
    Returns:
        bool: True if 'line' is the end of the project, otherwise False
    """
    return "-" * 10 in line


def handle_projects(projects):
    """
    1. Removes empty projects.
    2. Removes leading or trailing whitespaces.

    Args:
        projects (list): all the projects
    Returns:
        list: revised projects
    """
    return [project.strip() for project in projects if project.strip()]


def classify_resume(lines):
    """
    Classifies contents of resume into parts and revise formats.

    Args:
        lines (list): all lines in resume
    Returns:
        dict: resume info classified by parts of resume
    """
    resume = {
        "name": "",
        "email": "",
        "courses": [],
        "projects": []
    }
    is_project = False
    projects_lines = []

    for idx, line in enumerate(lines):
        # detects the first line as a name
        if idx == 0:
            resume["name"] = handle_name(line)
        else:
            # when the line is an email
            if detect_email(line):
                resume["email"] = handle_email(line)
            # when the line is courses
            elif detect_courses(line):
                resume["courses"] = handle_courses(line)
            # when the line is the start of projects
            elif detect_projects_start(line):
                is_project = True
                continue
            # when the line is the end of projects
            elif detect_projects_end(line):
                is_project = False

        # if the line in projects, appends it to list
        if is_project:
            projects_lines.append(line)

    # handles the format of projects
    resume["projects"] = handle_projects(projects_lines)
    return resume


def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.

    Args:
        tag (str): type of html tag
        text (str): html contents
    Returns:
        str: 'text' surrounded with 'tag' in html format
    """
    return f"<{tag}>{text}</{tag}>"


def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Args:
        email_address (str):

    Example:
        Given the email address: lbrandon@wharton.upenn.edu
        Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note:
        If, for some reason the email address does not contain @,
        use the email address as is and don't replace anything.
    """
    email_at = email_address.replace("@", "[aT]")
    return f"<a href=\"mailto:{email_address}\">{email_at}</a>"


def write_html_contents(html_template, resume):
    """
    Args:
        html_template (str): template html file path
        resume (dict): resume contents classified by parts
    Returns:
        str: resume in html format
    """
    # read the template file and remove the last two tags
    lines = read_file(html_template)
    html_lines = lines[:-2]

    # add the first line
    html_lines.append("<div id=\"page-wrap\">\n")

    # make the basic information section
    name = surround_block("h1", resume["name"])
    email_address = create_email_link(resume["email"])
    email = surround_block("p", f"Email: {email_address}")

    basic_info_section = surround_block("div", name + email)
    html_lines.append(basic_info_section + "\n")

    # make the projects section
    if resume["projects"]:
        title_projects = surround_block("h2", "Projects")
        project_names = ""
        for project in resume["projects"]:
            project_names += surround_block("li", project)
        projects = surround_block("ul", project_names)

        projects_section = surround_block("div", title_projects + projects)
        html_lines.append(projects_section + "\n")

    # make the courses section
    if resume["courses"]:
        title_courses = surround_block("h3", "Courses")
        courses_names = ", ".join(resume["courses"])
        courses = surround_block("span", courses_names)

        courses_section = surround_block("div", title_courses + "\n" + courses + "\n")
        html_lines.append(courses_section + "\n")

    # close tags
    close_tags = ["</div>", "</body>", "</html>"]
    html_lines += close_tags

    return "".join(html_lines)


def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """
    # make resume contents in html format
    lines = read_file(txt_input_file)
    resume = classify_resume(lines)
    html_contents = write_html_contents("resume_template.html", resume)

    # create new html file with 'html_contents'
    with open(html_output_file, "w") as f:
        f.write(html_contents)


def main():
    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file


if __name__ == '__main__':
    main()
