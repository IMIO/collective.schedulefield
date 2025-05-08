# collective.schedulefield

Schedule behaviors for Plone content types.

## Features

- Schedule or multi-schedule (with date ranges) behaviors to define schedules (morning / afternoon / comment) by day of week
- Exceptional closure behavior to define closing days

## Installation

Install `collective.schedulefield` by adding it to your buildout:

```ini
[buildout]

...

eggs =
    collective.schedulefield
```

Then run:

```bash
bin/buildout
```

## Compatibility

* Versions **1.x** are developed for **Plone 6**.
* Versions **0.x** are developed for **Plone 4 & Plone 5**.

  > Please note that they do not provide the full functionality (no multi-schedules,
  > no exceptional closures, no RESTAPI serializer).

## Contribute

Have an idea? Found a bug? Let us know by [opening a ticket](https://github.com/IMIO/collective.schedulefield/issues).

* **Issue Tracker**: [https://github.com/IMIO/collective.schedulefield/issues](https://github.com/IMIO/collective.schedulefield/issues)
* **Source Code**: [https://github.com/IMIO/collective.schedulefield](https://github.com/IMIO/collective.schedulefield)

## License

The project is licensed under the **GPLv2**.
