# Carte Multi
================

## Overview
------------

Carte Multi is a Python script designed to generate tickets with IDs. The script allows users to customize the font, text size, and color of the tickets, as well as the number of tickets per page.

## Background
-------------

I built Carte Multi to solve a specific problem: I needed to generate a large number of tickets with unique IDs for an event. I found that existing solutions were either too expensive or too complicated, so I decided to create my own script.

## Problem Statement
-------------------

I needed to generate 300 tickets with IDs ranging from 001 to 300, with 4 tickets per Word document page. I wanted a solution that was easy to use, customizable, and efficient.

## Solution
------------

Carte Multi is a Python script that uses the `docx` library to generate Word documents and the `PIL` library to add images and text to the tickets. The script allows users to:

* Select an image file (PNG or JPG) as the background for the tickets
* Enter the start and end numbers for the ticket IDs
* Choose a font and text size for the ticket IDs
* Enter the text color and position for the normal and reversed text
* Generate 4 tickets per Word document page

## Features
--------

* Generate tickets with IDs
* Customizable font, text size, and color
* Reversed text option
* Supports PNG and JPG image files
* Generates 4 tickets per Word document page

## Installation
------------

### Step 1: Install the required dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Download the font directory

Please download the font directory and place it in the same directory as the script.

## Usage
-----

### Step 1: Run the script

```bash
python cartemulti.py
```

### Step 2: Follow the instructions provided by the script

* Select an image file (PNG or JPG)
* Enter the start and end numbers for the ticket IDs
* Choose a font and text size
* Enter the text color and position for the normal and reversed text

## Contributing
------------

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
-------

This project is licensed under the [MIT License](LICENSE).

I hope this updated version meets your needs! Let me know if you have any further requests.