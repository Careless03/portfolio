# West Point Coding Portfolio

This repository is a curated portfolio of coursework and projects completed at West Point. It is organized by course area, with each folder containing assignments, reports, code, and supporting assets.

## Structure at a glance
- `Algorithms/`: Scala-based homework sets for algorithms.
- `Artificial Intelligence/`: Pacman projects, search, inference, and reinforcement learning, plus a Lunar Lander DQN project.
- `Basic Python Problem Sets/`: Intro Python problem sets and supporting data files.
- `Building_a_Game/`: Scala-based treasure hunt game project.
- `Databases/`: Django web app project and database backup.
- `Networks/`: Networking projects (UDP pinger, web server, Scapy/ICMP work).
- `Programming Languages/`: Scala assignments and language-related homework.

## Common file types and tooling
- `*.scala`: Scala solutions or project source code.
- `build.sbt`, `project/`, `.scalafmt.conf`: SBT build configuration and formatting rules.
- `*.tests`, `root.json`, `sbt.json`, `bloop.settings.json`, `.metals/`: Autograder, SBT, Bloop, and IDE metadata.
- `target/`, `__pycache__/`, `*.pyc`: Build or bytecode artifacts.
- `*.zip`: Turn-in bundles or provided starter files.
- `*.pdf`, `*.docx`: Reports, writeups, or assignment directions.

## Detailed contents

### Algorithms
Each `hw*-Careless03/` folder contains an SBT project with a main Scala solution file and supporting data.
- `hw1-Careless03/`: `hw1.scala`, `a.txt` input, SBT config, `README.md`, and IDE metadata; includes a `bash.exe.stackdump` log.
- `hw2-Careless03/`: `hw2.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw3-Careless03/`: `hw3.scala`, `a.txt`, `analysis.pdf`, SBT config, tests, and IDE metadata.
- `hw4-Careless03/`: `hw4.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw5-Careless03/`: `hw5.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw6-Careless03/`: `hw6.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw7-Careless03/`: `hw7.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw8-Careless03/`: `hw8.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw9-Careless03/`: `hw9.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw10-Careless03/`: `hw10.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw11-Careless03/`: `hw11.scala`, maze or grid inputs (`7x15.txt`, `15x31.txt`, `23x57.txt`, `test1.txt`), SBT config, and `turnin_hw11.zip`.

### Artificial Intelligence
- `DFS_BFS_Practice/`: Intro search practice with `addition.py`, `buyLotsOfFruit.py`, `shopSmart.py`, and autograder/test utilities.
- `Lunar_Landing_Project/`: DQN-based RL for Lunar Lander (`dqn.py`, `eval_dqn.py`, `QNetwork.py`, `requirements.txt`); `Clymer/` contains a run directory and copies of the model code; `Clymer.zip` is the submission bundle.
- `Pacman_A_Star_Search/`: Pacman search project with `search.py`, `searchAgents.py`, `pacman.py`, layouts (`*.lay`), `test_cases/`, and command scripts; `Clymer_Project1.zip` is the submission bundle.
- `Pacman_Advesarial_Search/`: Minimax/alpha-beta project with `multiAgents.py`, Pacman engine files, layouts, and `CLYMER_CS486_PROJECT 2.pdf` writeup; `clymer.zip` is the submission bundle.
- `Pacman_Inference_Learning/`: Ghost tracking and inference project with `inference.py`, `busters.py`, agent files, layouts, and test classes.
- `Pacman_Self_Learning/`: Reinforcement learning project with `qlearningAgents.py`, `valueIterationAgents.py`, `analysis.py`, Gridworld utilities, and layouts; `Clymer/` contains solution copies.

### Basic Python Problem Sets
- `ps01/`: `light_time.py`, `monthly_payment.py`, `spell_out_time.py`.
- `ps02/`: `aden_clymer_ps02_H.py`.
- `ps03/`: `aden_clymer_ps03_H.py`.
- `ps04/`: `aden_clymer_ps04_H.py` plus text inputs and logs (e.g., `elend.txt`, `server_status.log`).
- `ps05/`: `aden_clymer_ps05_H.py` and `words.txt`.
- `ps06/`: `ps06.py`, `playground.py`, and example inputs.
- `ps07/`: `aden_clymer_ps07_H.py`, sample text files, and `tester.csv`.
- `ps08/`: `aden_clymer_ps08_H.py` and `NHL_2018_test.csv`.
- `ps09/`: `aden_clymer_ps09_H.py`, `eBook.py`, and `Untitled-1.py`.
- Root-level coversheets are stored as `*.docx` and `*.pdf`.

### Building_a_Game
Scala game project (Treasure Hunt) with MVC-style source code and tests.
- `build.sbt`: SBT build definition.
- `src/main/scala/`: Game logic and UI (`Main.scala`, `Controller.scala`, `Model.scala`, `Board.scala`, `Cell.scala`, `Player.scala`, `Tile.scala`, strategies, and view classes).
- `src/test/scala/`: Unit tests (`LoginSecurityTest.scala`, `Menu_Test.scala`).
- `README.md`: Game rules and player strategies.

### Databases
Django project with an app and database backup.
- `manage.py`: Django management entry point.
- `final_app/`: App code (`models.py`, `views.py`, `forms.py`, `urls.py`, `tests.py`).
- `final_proj/`: Project settings (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`).
- `backup.sql`: Database snapshot.
- `README.txt`: Setup and run instructions.
- `.venv/` and `.vscode/`: Local environment and editor settings.

### Networks
- `project 1/`: UDP pinger assignment with `Project1_UDPPinger_v2_4.pdf` and `Analysis.docx`.
- `project2/`: Web server project with Python server (`project2_server.py`, `project2_server_starter.py`), HTML pages, and `CY350_proj_webserver_part2_v3.pdf`.
- `project3/`: Scapy/ICMP project with `scapy_client_starter.py`, `scapy_icmp_server_standalone`, and message/config files.
- `project3_2/`: `part2_starter_files.zip` provided starter pack.

### Programming Languages
Homework sets focused on Scala and language tooling.
- `hw1-Careless03/`: `hw1.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw2-Careless03/`: `hw2.txt`, `hw2results.txt`, regex checker tools (`regcheck.jar`, `regcheck.bat`, `regchk`).
- `hw3-Clymer/`: `hw3.scala`, SBT config, and `README.md`.
- `hw4-Clymer/`: `hw4.scala`, SBT config, tests, and IDE metadata.
- `hw5/`: `hw5.scala`, `a.txt`, SBT config, tests, and `work_cited.pdf`.
- `hw8/`: `hw8.scala`, `a.txt`, SBT config, and `cited-hw8.pdf`.
- `hw10/`: `hw10.scala`, `a.txt`, SBT config, and IDE metadata.
- `hw11/`: `hw11.scala`, `a.txt`, SBT config, tests, and IDE metadata.
- `hw13/`: `hw13.scala`, `a.txt`, SBT config, tests, and IDE metadata.

## Notes
This portfolio includes both source files and build artifacts (for example, `target/`, `__pycache__/`, `.metals/`). If you want a cleaned or curated version, those directories can be excluded.
