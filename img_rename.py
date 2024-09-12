import os


def images_fix(lab_report: str) -> str:
    fig_num = 1
    the_problem = "{#fig:001 width=70%}"
    new_lab_report = ''
    for line in lab_report.split("\n"):
        if the_problem in line:
            result = line.split(the_problem)
            new_num = f"{'0' * (3 - len(str(fig_num)))}{fig_num}"
            new_line = result[0] + "{" + "#fig:{0} width=70%".format(new_num) + "}"
            line = new_line
            fig_num += 1
        new_lab_report += f"\n{line}"
    return new_lab_report


def main():
    labs_path = r"C:\Users\maria\PycharmProjects\study_2023-2024_os-intro\labs"
    for lab in os.listdir(labs_path):
        if not "lab" in lab:
            continue
        report_path = os.path.join(labs_path, f"{lab}\\report\\report.md")
        with open(report_path, mode="r", encoding='utf-8') as f:
            lab_report = f.read()

        new_lab_report = images_fix(lab_report)

        with open(report_path, mode="w", encoding='utf-8') as f:
            f.write(new_lab_report)

if __name__ == "__main__":
    main()
