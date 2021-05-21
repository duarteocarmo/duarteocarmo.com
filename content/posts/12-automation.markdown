title:  Report Automation using Python, Papermill and Rclone
date:   2019-7-29 20:43:05 +0000

During the month of July I wrote two blog posts for the popular [Practical Business Python blog](https://pbpython.com/). The Practical Business Python blog is one of the top 20 most popular blogs on python with about [200.000 visits](https://www.similarweb.com/website/pbpython.com#overview) per month. 

The posts focus on how you can build an automation system that generates `Html` reports from excel files. The system uses python, jupyter, papermill, spruces and Rclone. 

Here are the links to both parts:

- [Part 1: Concept presentation](https://pbpython.com/papermil-rclone-report-1.html)
- [Part 2: Architecture and final solution](https://pbpython.com/papermil-rclone-report-2.html)

These posts were featured in the [Python Bytes podcast](https://pythonbytes.fm/episodes/show/142/there-s-a-bandit-in-the-python-space) (jump to 12:39):

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/662152787&color=%232a7ae2&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true">
</iframe>
<br/>
The architecture of the automation solution and final script follow:
<center>
<img src="{static}/images/architecture.png" alt="JupyterLab" style="width:90%; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);">
</center>
<br/>


Here is the code I used to automatically sync the reports on server:

```python
import subprocess
import sys
import papermill as papermill


REMOTE_FOLDER = "your cloud folder name"
LOCAL_FOLDER = "your local folder name"
TEMPLATE_NOTEBOOK = "template_notebook.ipynb"


def get_new_files(remote_folder, local_folder):
    """
    A function that returns files that were uploaded to the cloud folder and 
    do not exist in our local folder. 
    """
    # list the files in our cloud folder
    list_cloud = subprocess.run(
        ["rclone", "lsf", f"remote:{remote_folder}"],
        capture_output=True,
        text=True,
    )

    # transform the command output into a list
    cloud_directories = list_cloud.split("\n")[0:-1]

    print(f"In the cloud we have: \n{cloud_directories}")

    # list the files in our local folder
    list_cloud = subprocess.run(
        ["ls", local_folder], capture_output=True, text=True
    )

    # transform the command output into a list
    local_directories = list_cloud.stdout.split("\n")[0:-1]

    print(f"In the local copy we have: \n{local_directories}")

    # create a list with the differences between the two lists above
    new_files = list(set(cloud_directories) - set(local_directories))

    return new_files


def sync_directories(remote_folder, local_folder):
    """
    A function that syncs a remote folder with a local folder
    with rclone. 
    """
    sync = subprocess.run(
        ["rclone", "sync", f"remote:{remote_folder}", local_folder]
    )

    print("Syncing local directory with cloud....")
    return sync.returncode


def run_notebook(excel_report, template_notebook):
    """
    A function that runs a notebook against an excel report
    via papermill. 
    """
    no_extension_name = excel_report.split(".")[0]
    papermill.execute_notebook(
        template_notebook,
        f"{no_extension_name}.ipynb",
        parameters=dict(filename=excel_report),
    )
    return no_extension_name


def generate_html_report(notebook_file):
    """
    A function that converts a notebook into an html
    file. 
    """
    generate = subprocess.run(
        ["jupyter", "nbconvert", notebook_file, "--to=html"]
    )
    print("HTML Report was generated")
    return True


def push_to_cloud(remote_folder, filename):
    """
    A function that pushes to a remote cloud folder
    a specific file. 
    """

    push = subprocess.run(
        ["rclone", "copy", filename, f"remote:{remote_folder}"]
    )
    print("Report Published!!!")

def main():
    print("Starting updater..")

    # detect if there are new files in the remote folder
    new_files = get_new_files(
        remote_folder=REMOTE_FOLDER, local_folder=LOCAL_FOLDER
    )

    # if there are none, exit
    if not new_files:
        print("Everything is synced. No new files.")
        sys.exit()
    # else, continue
    else:
        print("There are files missing.")
        print(new_files)

    # sync directories to get new excel report
    sync_directories(remote_folder=REMOTE_FOLDER, local_folder=LOCAL_FOLDER)

    # generate new notebook and extract the name
    clean_name = run_notebook(new_files[0])

    # the new notebook generate will have the following name
    notebook_name = f"{clean_name}.ipynb"

    # generate the html report from the notebook
    generate_html_report(notebook_name)

    # the notebook name will be the following
    html_report_name = f"{clean_name}.html"

    # push the new notebook to the cloud
    push_to_cloud(html_report=html_report_name, remote_folder=ONEDRIVE_FOLDER)

    # make sure everything is synced again
    sync_directories(remote_folder=REMOTE_FOLDER, local_folder=LOCAL_FOLDER)

    print("Updater finished.")

    return True


if __name__ == "main":
    main()
```