# Buying List

A small tool to manage and organize articles to buy in lists. It uses an django backend with an REST API and a react frontend. It is meant to be an educational project.

## Contents

- [About the project](#About)
  - [Project Features](#Features)
- [How to set it up](#Setup)
- [How to use the app](#Use)
- [Technologies used](#Technologies)
  - [Frontend Technologies](#Frontend)
  - [BackEnd Technologies](#Backend)
  - [General Technologies](#General)

## About

This project is meant to help you organize and plan your everyday and extended shopping. You can create new articles with related price, category, tags, priority and so on. You can generate lists out of articles and caclculate possible prices.

### Features

**Implemented**

- None

**Planned**
- **Show articles** Shows either an specific Article by Id or all Articles, maybe also extended querying
- **Create Article** Saves a new article, might already have some valdation
- **Edit Article** Can alter properties of a certain article
- **Buy article** archives an article and mark it as bought.

**Backlog**

- **Reoccurring articles** Articles that need to be bought repeatedly in a certain timeframe
- **Dependcies Meaning** before Article A can be bought, first Article B should be bought
- **Buying Lists** Set an article based on price, tags, categories or dependencies on a list to buy them
- **Calculate Cost** Calculates the total cost of all articles, of articles of a categorie, of an article with all of its dependencies and of an list


## Setup

TODO: Add dockerization of the project and simple bashscripts to control them.

## Use

TODO

## Technologies

### Frontend

The frontend uses the [react framework](https://reactjs.org/). Additional dependencies are:

### Backend

The Backend uses the [django framework](https://www.djangoproject.com/). Additional dependencies are:

- [Django Restframework](https://www.django-rest-framework.org/)
- [TOX](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/)
- [Poetry](https://python-poetry.org/)

### General

The project uses [Docker](https://www.docker.com/) for deploment.
