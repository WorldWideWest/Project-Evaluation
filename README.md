# Investment Project Evaluation

## Table of Content's:
* [General-Info](#general-info)
* [Techonologies](#technologies)

## General Info

The project is based on Financial Mathematics and Business Finance and is there to automate the tasks of getting the right information about the Investment Project Info. 

I. The first part of the project 

First thing in this part is to crate a scalable table (pandas dataFrame), which will contain all the nececary data for the further processe's.

That include's getting the information:


<table>
    <thead>
        <tr>
            <td>Number</td>
            <td>Task</td>
            <td>Status</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1.</td>
            <td>Period of return</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>Discounted period of return</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>Net Present Value (NPV)</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>Internal rate of return (IRR)</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>5.</td>
            <td>Profitability Index (PI)</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>6.</td>
            <td>Method of annuity</td>
            <td>✅</td>
        </tr>
    </tbody>
</table>


Also every time something is added to the main code base, everyone must writte test's for that feature, which is included in the testing.py file. The test than are runned on GitHub Actions to make sure that our app is stable and ready to deploy.

The testing workflow you can find in <code>.github/workflows/ci.yml</code>

All the thing that are refferenced in some way you can find in the refference section of this file.


## Technologies
* Python 3.8.3 (https://www.python.org/)
* Jupyter Notebook (https://jupyter.org/)
* Visual Studio Code (https://code.visualstudio.com/)
* Git & GitHub (https://github.com/)
* Windows Subsystem for Linux (WSL2) (https://docs.microsoft.com/en-us/windows/wsl/wsl2-index)





## Refferences
* Django (https://www.djangoproject.com/)
* TensorFlow (https://www.tensorflow.org/)
* Python (https://www.python.org/)
* Jupyter Notebook (https://jupyter.org/)
* Visual Studio Code (https://code.visualstudio.com/)
* Git & GitHub (https://github.com/)
* Windows Subsystem for Linux (WSL2) (https://docs.microsoft.com/en-us/windows/wsl/wsl2-index)



