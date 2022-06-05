# Luke's Garzia Resume - CLI App

This represents a weekend project to make writing a resume a tad more interesting.
Specifically --- I wanted to turn the resume into a CLI app and post on pypi.

## Installation

```shell
>> pip install luke-resume
```

## Usage

There two commands:

- Display in terminal `luke display-resume`
- Open pdf version of resume `luke open-resume`

### Display resume in terminal

Scroll through whole resume

```shell
>> luke display-resume
```

![Display Resume Example](https://github.com/lgarzia/resume/blob/main/docs/source/_static/luke_full_resume.gif)

## Additional flag is `--num-prev-jobs 3`

View an abridged edition

```shell
>> luke display-resume --abridged
```

![Display Abridged Resume](https://github.com/lgarzia/resume/blob/main/docs/source/_static/luke_display_abridged2.gif)

---

### Open pdf version of resume

Open full copy of resume

```shell
>>luke open-resume
```

![Open PDF Resume](https://github.com/lgarzia/resume/blob/main/docs/source/_static/luke_open_resume.gif)

Alternative is `luke open-resume --method web`
