import unittest
from make_website import *


class MakeWebsite_Test(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(["This\n", "is\n", "a test"], read_file("test_read_file.txt"))

    def test_handle_name(self):
        # test name with whitespace
        self.assertEqual("Soohyun Choi", handle_name("    Soohyun Choi  "))
        # test name starting with a lowercase letter
        self.assertEqual("Invalid Name", handle_name("soohyun Choi"))
        # test name starting with a punctuation
        self.assertEqual("Invalid Name", handle_name("@Soohyun Choi"))

    def test_detect_email(self):
        # test line with @ sign
        self.assertEqual(True, detect_email("test@test"))
        # test line without @ sign
        self.assertEqual(False, detect_email("test"))
        # test empty line
        self.assertEqual(False, detect_email(""))

    def test_handle_email(self):
        # test email with whitespace
        self.assertEqual("test@test.com", handle_email("  test@test.com  "))
        # test email (not) ending with .com or .edu
        self.assertEqual("test@test.com", handle_email("test@test.com"))
        self.assertEqual("test@test.edu", handle_email("test@test.edu"))
        self.assertEqual("", handle_email("test@test.io"))
        # test email not starting with a lowercase letter after @ sign
        self.assertEqual("", handle_email("test@.com"))
        # test email with numbers
        self.assertEqual("", handle_email("test1@test.com"))
        self.assertEqual("", handle_email("test@test2.com"))

    def test_detect_courses(self):
        # test line with "Courses"
        self.assertEqual(True, detect_courses("test_Courses-test"))
        # test line without "Courses"
        self.assertEqual(False, detect_courses("test"))

    def test_handle_courses(self):
        # test courses with whitespace at the beginning or the end of the whole line
        self.assertEqual(["test1", "test2", "test3"],
                         handle_courses("   Courses : test1, test2, test3  "))
        # test courses with whitespace before and after , sign
        self.assertEqual(["test1", "test2", "test3"],
                         handle_courses("Courses : test1  , test2 ,  test3"))
        # test courses with various punctuations
        self.assertEqual(["test1", "test2", "test3"],
                         handle_courses("Courses   #-:=,/@  test1, test2, test3"))
        # test courses starting with number
        self.assertEqual(["test1", "test2", "test3"],
                         handle_courses("Courses : 2test1, test2, test3 "))
        # test courses with punctuations in actual course names
        self.assertEqual(["te#st1", "!test/2", "test3?"],
                         handle_courses("Courses : te#st1, test/2, test3? "))
        # test courses without actual course names
        self.assertEqual([], handle_courses("Courses : "))

    def test_detect_project_start(self):
        # test line with "Projects"
        self.assertEqual(True, detect_projects_start("test_Projects-test"))
        # test line without "Projects"
        self.assertEqual(False, detect_projects_start("test"))

    def test_detect_project_end(self):
        # test line with ten - signs
        self.assertEqual(True, detect_projects_end("-" * 10))
        # test line with more than ten - signs
        self.assertEqual(True, detect_projects_end("-" * 20))
        # test line with less than ten - signs
        self.assertEqual(False, detect_projects_end("----"))
        # test line with more than ten - signs but nonconsecutive
        self.assertEqual(False, detect_projects_end("---  -----test----"))

    def test_handle_projects(self):
        self.assertEqual(["test1", "test2", "test3"],
                         handle_projects(["  test1 ", " test2  ", " test3 "]))

    def test_classify_resume(self):
        # test lines with all parts
        self.assertEqual(
            {
                "name": "Soohyun Choi",
                "email": "soohyun@upenn.edu",
                "courses": ["course1", "course2", "course3"],
                "projects": ["project1", "project2", "project3"]
            },
            classify_resume([
                "Soohyun Choi",
                "Courses :- course1, course2, course3",
                "Projects",
                "project1",
                "project2",
                "project3",
                "------------------------------",
                "soohyun@upenn.edu"
            ])
        )
        # test lines without the email part
        self.assertEqual(
            {
                "name": "Soohyun Choi",
                "email": "",
                "courses": ["course1", "course2", "course3"],
                "projects": ["project1", "project2", "project3"]
            },
            classify_resume([
                "Soohyun Choi",
                "Courses :- course1, course2, course3",
                "Projects",
                "project1",
                "project2",
                "project3",
                "------------------------------"
            ])
        )
        # test lines without the courses part
        self.assertEqual(
            {
                "name": "Soohyun Choi",
                "email": "soohyun@upenn.edu",
                "courses": [],
                "projects": ["project1", "project2", "project3"]
            },
            classify_resume([
                "Soohyun Choi",
                "Projects",
                "project1",
                "project2",
                "project3",
                "------------------------------",
                "soohyun@upenn.edu"
            ])
        )
        # test lines without the projects parts
        self.assertEqual(
            {
                "name": "Soohyun Choi",
                "email": "soohyun@upenn.edu",
                "courses": ["course1", "course2", "course3"],
                "projects": []
            },
            classify_resume([
                "Soohyun Choi",
                "Courses :- course1, course2, course3",
                "soohyun@upenn.edu"
            ])
        )

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>", surround_block('h1', 'Eagles'))
        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))

    def test_create_email_link(self):
        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )
        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )
        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )

    def test_create_html_basic_info_sections(self):
        self.assertEqual(
            "<div><h1>name</h1><p>Email: <a href=\"mailto:email\">email</a></p></div>",
            create_html_basic_info_sections("name", "email")
        )

    def test_creat_html_projects(self):
        self.assertEqual(
            "<div><h2>Projects</h2><ul><li>project1</li><li>project2</li></ul></div>",
            create_html_projects(["project1", "project2"])
        )

    def test_create_html_courses(self):
        self.assertEqual(
            "<div><h3>Courses</h3><span>course1, course2</span></div>",
            create_html_courses(["course1", "course2"])
        )

    def test_create_html_contents(self):
        with open("resume_template.html", "r") as f:
            lines = f.readlines()

        self.assertEqual(
            f"{''.join(lines[:-2])}<div id=\"page-wrap\">\n"
            + f"{create_html_basic_info_sections('Soohyun Choi', 'soohyun@upenn.edu')}\n"
            + f"{create_html_projects(['project1', 'project2'])}\n"
            + f"{create_html_courses(['course1', 'course2'])}\n"
            + "</div></body></html>",
            create_html_contents("resume_template.html",
                                {
                                    "name": "Soohyun Choi",
                                    "email": "soohyun@upenn.edu",
                                    "courses": ["course1", "course2"],
                                    "projects": ["project1", "project2"]
                                })
        )
        # test resume without courses
        self.assertEqual(
            f"{''.join(lines[:-2])}<div id=\"page-wrap\">\n"
            + f"{create_html_basic_info_sections('Soohyun Choi', 'soohyun@upenn.edu')}\n"
            + f"{create_html_projects(['project1', 'project2'])}\n"
            + "</div></body></html>",
            create_html_contents("resume_template.html",
                                 {
                                     "name": "Soohyun Choi",
                                     "email": "soohyun@upenn.edu",
                                     "courses": [],
                                     "projects": ["project1", "project2"]
                                 })
        )
        # test resume without projects
        self.assertEqual(
            f"{''.join(lines[:-2])}<div id=\"page-wrap\">\n"
            + f"{create_html_basic_info_sections('Soohyun Choi', 'soohyun@upenn.edu')}\n"
            + f"{create_html_courses(['course1', 'course2'])}\n"
            + "</div></body></html>",
            create_html_contents("resume_template.html",
                                 {
                                     "name": "Soohyun Choi",
                                     "email": "soohyun@upenn.edu",
                                     "courses": ["course1", "course2"],
                                     "projects": []
                                 })
        )


if __name__ == '__main__':
    unittest.main()
