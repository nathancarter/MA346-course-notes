
# VS Code for Python Installation

This assumes you have [installed Anaconda](anaconda-installation) already.

## Open the Anaconda Navigator

Start Menu \> Anaconda3 \> Anaconda Navigator\
(On Mac: Finder \> Applications \> Anaconda Navigator.app.)

<img alt="A screenshot of the main window for the Anacdona Navigator application
on Windows, showing icons for the applications JupyterLab, Jupyter
Notebook, Spyder, VS Code, Glueviz, and Orange
3." src="../../_images/install-image-6.png" class="center-box-image"/>


## Find and Install the VS Code application

Scroll down in the list of applications until you find VS Code (Visual
Studio Code, by Microsoft).

<img alt="The VS Code application tile as it would appear in the Anaconda
Navigator main window, with an &quot;Install&quot; button beneath
it" src="../../_images/install-image-7.png" class="center-box-image"/>


Click the Install button beneath it.

Once you have installed VS Code, its application icon will change to
contain a "Launch" button.

<img alt="The VS Code application tile as it would appear in the Anaconda
Navigator main window, with a &quot;Launch&quot; button beneath
it" src="../../_images/install-image-8.png" class="center-box-image"/>


Click that button now to launch VS Code.

## Installing and Configuring Code Runner

VS Code is all ready to let you edit Python code, but there's an
Extension to VS Code, called Code Runner, that makes it more convenient
to run Python code when testing your work. Let's install it now.

Click the Extensions button on the left of the VS Code window.  It is the bottom button shown below, which looks like four squares:

<img alt="A screenshot of the icons on the left edge of the VS Code window,
showing icons for Explorer (two file icons), Search (magnifying glass
icon), Source Control (small graph icon), Debug (insect icon), and
Extensions (small blocks
icon)" src="../../_images/install-image-9.png" class="center-box-image"/>


Then search for the Code Runner Extension as shown below and click its
install button.  (The install button is green and is just below and to the right of hte large orange ".run" icon.)

<img alt="Screenshot of most of the VS Code window during the installation of
the Code Runner Extension, including the Extension\'s
description" src="../../_images/install-image-10.png" class="center-box-image"/>

The Code Runner Extension in the Extensions list will then have a
settings gear icon, as shown below.

<img alt="" src="../../_images/install-image-11png" class="center-box-image"/>

Click that gear icon to bring up the settings menu for Code Runner, as shown below.

<img alt="" src="../../_images/install-image-12.png" class="center-box-image"/>

Choose "Configure Extension Settings," the bottom item on that menu.

It will bring up a settings window as shown below.

<img alt="" src="../../_images/install-image-13.png" class="center-box-image"/>

Scroll down until you find the settings for saving files before running,
and check both boxes, as shown here.

<img alt="A small portion of the list of settings for the Code Runner Extension in VS Code, highlighting just the two settings relevant for saving files before running them, both of which are checked (enabled)" src="../../_images/install-image-14.png" class="center-box-image"/>

Your Code Runner Extension is correctly configured. Try it out as shown
on the next page.

## Testing your Installation

Let's verify now that you can successfully run Python code.

Create a new file:

<img alt="A screenshot of the File Menu in VS Code, with the &quot;New File&quot; item
selected" src="../../_images/install-image-15.png" class="center-box-image"/>

<img alt="" src="../../_images/install-image-16.png" class="center-box-image"/>

Save the file and give it the name `test.py` to indicate that it is a Python file.

<img alt="A screenshot of the File Menu in VS Code, with the &quot;Save As&quot; item selected" src="../../_images/install-image-17.png" class="center-box-image"/>

Enter the following small amount of Python code in the new, empty file.

*Be sure to press Enter after the code to start a new line!*

<img alt="A screenshot of a one-line Python program shown in the VS Code editor.  The Python program contains just the one command print( 2+2 )." src="../../_images/install-image-18.png" class="center-box-image"/>

Save the file again.

Run the file by clicking the small Run icon (which looks like a "Play"
triangle) on the top right of the window.  (If you don't see this button,
check your work above---did you save the file with a `.py` extension?)

<img alt="A screenshot of the upper right corner of the VS Code interface, after the Code Runner Extension has been installed, so that a triangular &quot;Play&quot; button appears, allowing the user to run the code in the current file" src="../../_images/install-image-19.png" class="center-box-image"/>

You should see the following output at the bottom of the window,
indicating that your code was run, and produced the output `4` (which is
the result of 2+2, of course).

<img alt="A screenshot showing the output of running the simply Python program shown earlier. The output includes a line indicating that Python was run, a single line of output containing the number 4, and a final line indicating that the code completed with code=0 in 0.102 seconds." src="../../_images/install-image-20.png" class="center-box-image"/>

(The first line means that the "python" command was run on the `test.py`
file you saved. The final line means the process ended with error code
0, which means no errors, and took 0.102 seconds in total.)

You have a successful Python installation that you can run from Visual
Studio!
