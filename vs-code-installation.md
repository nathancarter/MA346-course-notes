
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

## Adding Support for Jupyter Notebooks

VS Code is all ready to let you edit Python code, but much data work happen in
Jupyter notebooks rather than Python scripts.  Let's install a VS Code extension
to support Jupyter notebooks.

Click the Extensions button on the left of the VS Code window.  It is the bottom button shown below, which looks like four squares:

<img alt="A screenshot of the icons on the left edge of the VS Code window,
showing icons for Explorer (two file icons), Search (magnifying glass
icon), Source Control (small graph icon), Debug (insect icon), and
Extensions (small blocks
icon)" src="../../_images/install-image-9.png" class="center-box-image"/>

Then search for Jupyter, as shown in the search box below.  The first result,
also shown in the image, is the Jupyer extension made by Microsoft.  Once you've
verified that you're looking at the official extension made by Microsoft (as in
the image below), click its Install button.

<img alt="Screenshot of most of the VS Code window during the installation of
the Jupyter Extension, including the Extension\'s
description" src="../../_images/install-image-10.png" class="center-box-image"/>

## Testing your Installation

Let's verify now that you can successfully run Python code in a Jupyter notebook
in VS Code.

Create a new Jupyter notebook:

 1. Open the command palette (Windows: Ctrl+Shift+P, Mac: Command+Shift+P).
 2. Search for "notebook" as shown in the image below.
 3. Choose "Jupyter: Create New Blank Notebook," as shown in the image.

<img alt="A screenshot of the command palette in VS Code, with the &quot;Jupyter: Create New Blank Notebook&quot; item selected" src="../../_images/install-image-11.png" class="center-box-image"/>

Place your cursor in the first input cell of the notebook, as shown in the image
below, and type some very simple Python code, such as `1+1`.  Press Shift+Enter
to run the code, and you should see the output (obviously 2 in that case).

<img alt="A screenshot of a new Jupyter notebook in VS Code, with just the code 1+1 typed in the first cell" src="../../_images/install-image-12.png" class="center-box-image"/>

Feel free to save the notebook, but it is not necessary to do so; you can close
without saving after this brief test.

You have a successful Python and Jupyter installation that you can run from VS Code!
