import shutil
import os

create_docs = "{{ cookiecutter.create_docs }}"
module_name = "{{ cookiecutter.module_name }}"

if __name__ == "__main__":
    breakpoint()
    if not create_docs[0]:
        shutil.rmtree("docs", ignore_errors=True)
        os.remove(".github/workflows/check_docs.yml")
        os.remove(".github/workflows/publish_docs.yml")
        os.remove(f"{module_name}/greetings.py")
        os.remove(f"{module_name}/math.py")
    shutil.rmtree("licenses", ignore_errors=True)
