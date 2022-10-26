# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# A macro that turns every entry in this directory's requirements.txt into a
# `python_requirement_library` target. Refer to
# https://www.pantsbuild.org/docs/python-third-party-dependencies.
python_requirements(name = "reqs")

python_distribution(
    name = "test_distribution",
    dependencies = ["//helloworld/greet/greeting.py:lib"],
    entry_points = {"console_scripts": {"hello": "helloworld.greet.greating:say_hello"}},
    provides = python_artifact(
        name = "test_dist",
        version = "0",
    ),
)

pex_binary(
    name = "executable_scripts",
    dependencies = [
        ":test_distribution",
        ":reqs#conscript",
    ],
    script = "conscript",
)
