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



This part of the project will be based on CLI (Command Line Interface), once all of the funcionality wokr's without a problem will continue to the next part of the project.

II. Adding Deep Learning to the project

In this part will use Neural Nets to classify a project as [A, B, C].
This part will only take part if we have enaught training data.

III. Adding for the Balance Sheet

Here we will apply Financial knowledge to calculate Financial indicators of the company based on Balance Sheet's and Cash Flow Report's.

The indicators based on Balance Sheet's:
1. Indicators of liquidity and solvency
2. Indicators of depth
3. Indicators of activity
4. Indicators of profitability
5. Indicators of efficiency of investing

The indicators based on Cash Flow Report:
1. Indicators of liquidity and solvency
2. Indicators of quality of profit
3. Indicators of Capital expenditures
4. Indicators of Cash Flow return

We expcet to add Deep Learning to this part of the project if we have a big enaught dataset. 

IV. Getting online

This part is there to bring all of our logic to the Web. Let me explain, everythin that we would done so far is based in a CLI(Command Line Interface), that is because it is easy to debug and it is realy easy to keep track of the progress.

But no one wuld use a CLI so we need to make it user frendly, to do that we need a Web framework to publish our work in a user frendly enviroment. We are not yet sure which framework it would be, but when you use Python for your logic the only option for you is to use Django, if we don't see any radical change in the code base, which is a very low possibility, we will also role with Django.


The remaining info for this project is that we will use TensorFlow for our Deep Learning Framework. 

Also every time something is added to the main code base, everyone must writte test's for that feature, which is included in the test.py file. The test than are runned on GitHub Actions to make sure that our app is stable and ready to deploy.

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



