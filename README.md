# Game Work One

## Prerequisites

#### Install Homebrew

If you're a Mac user and you don't have [Homebrew](https://brew.sh/), you should download and install it.

#### Install Python

You will need Python installed. We recommend using [pyenv](https://github.com/pyenv/pyenv). Run the following command and then follow the instructions given.

```bash
brew install pyenv
```

Then, you'll want to install Python 3.6.3.

```bash
pyenv install 3.6.3
```

Finally, confirm that things are working correctly by checking the version of Python from within the app directory.

```bash
MacBook-Pro:game-work-one pedro$ pyenv version
3.6.3 (set by /Users/pedro/Projects/game-work-one/.python-version)

MacBook-Pro:game-work-one pedro$ python --version
Python 3.6.3
```

#### Install Additional System Packages

This app requires several other system packages to run. We maintain these within [our Brewfile](https://github.com/theDrinkMD/game-work-one/blob/master/Brewfile).

If you have [Homebrew](http://brew.sh/) installed, you can run `brew bundle` to install them.

## Setup

#### Install App Dependencies

```shell
pip install heroku honcho
pip install -r requirements.txt
```

#### Configuring Database

Nothing needed here yet, apparently.

## Starting Application

```shell
honcho start
```

Then visit to confirm the app is working:
`http://localhost:5000/api/question/`

## Running Tests

:(
