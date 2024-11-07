# Desktop-Organizer
This project automatically organizes files downloaded to the **Downloads** folder by categorizing them based on file type and moving them to specific folders on the **Desktop**. This script is particularly useful for keeping a tidy workspace and automatically organizing incoming files.

## Features

- **File Categorization**: Categorizes files into folders based on their types, such as **Images**, **Videos**, **Documents**, **Music**, **Archives**, **Scripts**, and **Others**.
- **Automatic Monitoring**: Uses the `watchdog` library to monitor the Downloads folder and automatically organizes files as soon as they are downloaded.

## Getting Started

### Prerequisites

- **Python 3 or above**: [Download Python](https://www.python.org/downloads/)
- **`watchdog` library: cmd `pip install watchdog`

### Quick Steps

1. Clone the GitHub repository to your local machine:
`$ git clone https://github.com/Justin-Liao23-e/Desktop-Organizer.git`
2. Run the script:
`python driver.py`
3. Monitor your **Downloads** and **Desktop** to see how the files are transfered and categorized. Try to download various file type from the internet.
Note: You may interupt by hitting `ctrl c`, else it runs forever unless you shut down your computer.

## License

This project is licensed under the MIT License.

## References:

1. https://docs.python.org/3/library/os.path.html#os.path.join
2. https://docs.python.org/3/library/shutil.html
3. https://pypi.org/project/watchdog/