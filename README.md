# Qiskit Terra
[![License](https://img.shields.io/github/license/Qiskit/qiskit-terra.svg?style=popout-square)](https://opensource.org/licenses/Apache-2.0)<!--- long-description-skip-begin -->[![Build Status](https://img.shields.io/travis/com/Qiskit/qiskit-terra/master.svg?style=popout-square)](https://travis-ci.com/Qiskit/qiskit-terra)[![Release](https://img.shields.io/github/release/Qiskit/qiskit-terra.svg?style=popout-square)](https://github.com/Qiskit/qiskit-terra/releases)[![Downloads](https://img.shields.io/pypi/dm/qiskit-terra.svg?style=popout-square)](https://pypi.org/project/qiskit-terra/)[![Coverage Status](https://coveralls.io/repos/github/Qiskit/qiskit-terra/badge.svg?branch=main)](https://coveralls.io/github/Qiskit/qiskit-terra?branch=main)<!--- long-description-skip-end -->

**Qiskit** is an open-source framework for working with noisy quantum computers at the level of pulses, circuits, and algorithms.

Qiskit is made up of elements that work together to enable quantum computing. This element is **Terra** and is the foundation on which the rest of Qiskit is built.

# PushQuantum Hackathon Presentation
We have cloned from the original Qiskit Terra repository and added new functionality to:
* remove targeted gates from a pre-defined quantum circuit,
    * qiskit/circuit/quantumcircuit.py - def remove_gates()
* implement a QFT circuit in its fully expanded form.
    * qiskit/circuit/library/basis_change/qft.py

## How did we get here?
Our initial idea was to add functionality to enable users to expand the quantum circuit drawing of a base circuit (e.g. QFT) from a
building block to a full display form. For example:
![Image of QFT Full/Compact](https://github.com/biblio-techers/Qiskit-Fall-Fest-2021/blob/nadeem_develop/Images/Example_Of_Decomposition.png)
As a next step we wanted to enable this functionality in the general case, and hence apply it to the quantum circuit class. This was 
when we realised that this functionality already exists in the form of the decompose method. However, this decompose method also
decomposes the Hadamard gates for our QFT example, so there are some minor differences.
## If at first, you don't succeed... try something else
Given that this functionality had already been implemented, we continued with our extension idea: "Provide a clean and friendly way to 
allow users to remove targeted gates from their quantum circuits". There is a brief discussion of how to currently do this in:
https://arxiv.org/abs/1903.04359
The advise in lesson 2 is to directly edit the quantumcircuit.data list based on the index of the gate that you want to move. This can be a complex thought process for the user and it is much more intuitive to pick a gate from the diagram that you want to remove. This becomes even more apparent when you consider the indexing structure of the data list is not unique if it contains single qubit gates.
## Functionality of the remove_gate method
The method takes two arguments, qubits, and gates_to_remove. Qubits are the qubits for which you want to target gate removal. gates_to_remove are the gates which you want to target for removal. These can either be strigs, indicating the names which you want to remove, or integers, indicating which gates along the circuit you want to remove. If both are present, then the function removes the specified gates only on the specified qubits. If none are present, then all gates are removed.
```python
for i in list(range(len(circuit.data)))[::-1]:
    for j in list(range(len(circuit.data[i][1])))[::-1]:
        if (circuit.data[i][1][j].index in qubits and 
            circuit.data[i][0].name in gates_to_remove):
            circuit.data.pop(i)
            break
```
The brains of this method comes from the above code snip, which reviews the data list of the quantum circuit, and identifies & removes the requied gate entries as specified by the user.
The function then returns an updated quantum circuit.

## Next steps
We would like to follow the object orientated style of the qiskit source code. This requires us to create the above method as a class inheriting from quantumcircuit and returning a removed_gates type object. This will allow us to:
* Reduce the amount of content in the quantumcircuit.py file given that it is already very large
* Keep to the convention of the qiskit source code such that our contribution fits nicely
* Take advantage of the object orientated structure of qiskit when we look to expand our contribution to more features. There are many more ways a user may want to remove gates from a circuit, each worthy of their own method.

## Future work and outlook
Removing gates is the simplest form of amending an existing quantum circuit given that it is well defined and has finite implementations. However, it would also be benifitial to the user to have a similar class/method to conduct other ciruit altering functions such as:
* Swapping gates,
* Adding gates at specified locations,
* Duplicating gates
After implementing the remove gates functionality as a class we look to extend this to the above use cases for as broad as possible implementation and potentially provide it as a mini feature update to the main qiskit-terra source code. We also welcome feedback and other ideas of analogous features to implement.



# Standard README.md documentation from Qiskit

## Installation

We encourage installing Qiskit via the pip tool (a python package manager), which installs all Qiskit elements, including Terra.

```bash
pip install qiskit
```

PIP will handle all dependencies automatically and you will always install the latest (and well-tested) version.

To install from source, follow the instructions in the [documentation](https://qiskit.org/documentation/contributing_to_qiskit.html#install-terra-from-source).

## Creating Your First Quantum Program in Qiskit Terra

Now that Qiskit is installed, it's time to begin working with Terra.

We are ready to try out a quantum circuit example, which is simulated locally using
the Qiskit BasicAer element. This is a simple example that makes an entangled state.

```
$ python
```

```python
>>> from qiskit import QuantumCircuit, transpile
>>> from qiskit.providers.basicaer import QasmSimulatorPy
>>> qc = QuantumCircuit(2, 2)
>>> qc.h(0)
>>> qc.cx(0, 1)
>>> qc.measure([0,1], [0,1])
>>> backend_sim = QasmSimulatorPy()
>>> transpiled_qc = transpile(qc, backend_sim)
>>> result = backend_sim.run(transpiled_qc).result()
>>> print(result.get_counts(qc))
```

In this case, the output will be:

```python
{'00': 513, '11': 511}
```

A script is available [here](examples/python/ibmq/hello_quantum.py), where we also show how to
run the same program on a real quantum computer via IBMQ.

### Executing your code on a real quantum chip

You can also use Qiskit to execute your code on a
**real quantum chip**.
In order to do so, you need to configure Qiskit for using the credentials in
your IBM Q account:

#### Configure your IBMQ credentials

1. Create an _[IBM Q](https://quantum-computing.ibm.com) > Account_ if you haven't already done so.

2. Get an API token from the IBM Q website under _My Account > API Token_ and the URL for the account.

3. Take your token and url from step 2, here called `MY_API_TOKEN`, `MY_URL`, and run:

   ```python
   >>> from qiskit import IBMQ
   >>> IBMQ.save_account('MY_API_TOKEN', 'MY_URL')
    ```

After calling `IBMQ.save_account()`, your credentials will be stored on disk.
Once they are stored, at any point in the future you can load and use them
in your program simply via:

```python
>>> from qiskit import IBMQ
>>> IBMQ.load_account()
```

Those who do not want to save their credentials to disk should use instead:

```python
>>> from qiskit import IBMQ
>>> IBMQ.enable_account('MY_API_TOKEN')
```

and the token will only be active for the session. For examples using Terra with real
devices we have provided a set of examples in **examples/python** and we suggest starting with [using_qiskit_terra_level_0.py](examples/python/using_qiskit_terra_level_0.py) and working up in
the levels.

## Contribution Guidelines

If you'd like to contribute to Qiskit Terra, please take a look at our
[contribution guidelines](CONTRIBUTING.md). This project adheres to Qiskit's [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

We use [GitHub issues](https://github.com/Qiskit/qiskit-terra/issues) for tracking requests and bugs. Please
[join the Qiskit Slack community](https://ibm.co/joinqiskitslack)
and use our [Qiskit Slack channel](https://qiskit.slack.com) for discussion and simple questions.
For questions that are more suited for a forum we use the Qiskit tag in the [Stack Exchange](https://quantumcomputing.stackexchange.com/questions/tagged/qiskit).

## Next Steps

Now you're set up and ready to check out some of the other examples from our
[Qiskit Tutorials](https://github.com/Qiskit/qiskit-tutorials) repository.

## Authors and Citation

Qiskit Terra is the work of [many people](https://github.com/Qiskit/qiskit-terra/graphs/contributors) who contribute
to the project at different levels. If you use Qiskit, please cite as per the included [BibTeX file](https://github.com/Qiskit/qiskit/blob/master/Qiskit.bib).

## Changelog and Release Notes

The changelog for a particular release is dynamically generated and gets
written to the release page on Github for each release. For example, you can
find the page for the `0.9.0` release here:

https://github.com/Qiskit/qiskit-terra/releases/tag/0.9.0

The changelog for the current release can be found in the releases tab:
[![Releases](https://img.shields.io/github/release/Qiskit/qiskit-terra.svg?style=popout-square)](https://github.com/Qiskit/qiskit-terra/releases)
The changelog provides a quick overview of notable changes for a given
release.

Additionally, as part of each release detailed release notes are written to
document in detail what has changed as part of a release. This includes any
documentation on potential breaking changes on upgrade and new features.
For example, You can find the release notes for the `0.9.0` release in the
Qiskit documentation here:

https://qiskit.org/documentation/release_notes.html#terra-0-9

## License

[Apache License 2.0](LICENSE.txt)
