# Deep Reinforcement Learning for Automated Stock Trading: An Ensemble Strategy
This repository provides codes for [ICAIF 2020 paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690996)

This ensemble strategy is reimplemented in a Jupiter Notebook at [FinRL](https://github.com/AI4Finance-LLC/FinRL-Library).


### Buoc 1 - Prerequisites
For [OpenAI Baselines](https://github.com/openai/baselines), you'll need system packages CMake, OpenMPI and zlib. Those can be installed as follows

#### Ubuntu

```bash
sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev libgl1-mesa-glx
```

#### Mac OS X
Installation of system packages on Mac requires [Homebrew](https://brew.sh). With Homebrew installed, run the following:
```bash
brew install cmake openmpi
```

#### Windows 10

To install stable-baselines on Windows, please look at the [documentation](https://stable-baselines.readthedocs.io/en/master/guide/install.html#prerequisites).
    
### Buoc 2 - Create and Activate Virtual Environment
cd into this repository
```bash
cd Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020
```
Under folder /Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020, create a virtual environment
```bash
pip install virtualenv
```
Virtualenvs are essentially folders that have copies of python executable and all python packages. 

**Virtualenvs can also avoid packages conflicts.**

Create a virtualenv **venv** under folder /Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020
```bash
virtualenv -p python3 venv
```
To activate a virtualenv:
```
source venv/bin/activate
```

## Buoc 3 - Dependencies

The script has been tested running under **Python >= 3.6.0**, with the folowing packages installed:

```shell
pip install -r requirements.txt
```
```bash
pip install tensorflow==1.15.4
```
```
pip install stable-baselines[mpi]
```
```
pip install stable-baselines
```


## Buoc 5 - Run DRL Ensemble Strategy

```shell
python run_DRL.py
```

## Buoc 6 - Backtesting


### Giai thich - Ensemble Strategy
Our purpose is to create a highly robust trading strategy. So we use an ensemble method to automatically select the best performing agent among PPO, A2C, and DDPG to trade based on the Sharpe ratio. The ensemble process is described as follows:
* __Step 1__. We use a growing window of 𝑛 months to retrain our three agents concurrently. In this paper we retrain our three agents at every 3 months.
* __Step 2__. We validate all 3 agents by using a 12-month validation- rolling window followed by the growing window we used for train- ing to pick the best performing agent which has the highest Sharpe ratio. We also adjust risk-aversion by using turbulence index in our validation stage.
* __Step 3__. After validation, we only use the best model which has the highest Sharpe ratio to predict and trade for the next quarter.
