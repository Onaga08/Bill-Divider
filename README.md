# Bill-Divider

<h2>Need for this</h2>
<p>Me and 4 of my friends live together in a flat. I, Pradyumn live alone in one room, and the other four live together as pairs in two other rooms. All of our rooms have ACs and the bill in the State of Tamil Nadu is quite high. All of us have uneven usage and it feels wrong to distribute the bill evenly. So we installed meters for the three AC's and had to devise a formula to distribute the bill according to the usage of the three meters.</p>

<h2>Pre-Requisite</h2>
<h3>Before you begin, make sure you have Python installed. Additionally, you need to install the `tkinter` module, which is usually included with Python.</h3>

```bash
pip install tk
```
<h3>Installation</h3>

Clone the repository and navigate to the project folder.
```bash
git clone https://github.com/Onaga08/Bill-Divider.git
cd Bill-Divider
```

<h3>Usage</h3>

To run the program
```bash
python main.py
```

**Underlying Math**

```math
Total Units: 100 '\n'
Total Bill : 1000/-
m1 : 50 units
m2: 100 units
m3: 200 units

Now, we find per unit cost => (Total Bill/ Total Units) => (1000/10) => 10 Rs/unit (avg)

We multiply this per unit cost with the cost of all the meters to find out how much each of the ACs have consumed. 
Accordingly we divide this among five roommates. 
Note - As I live alone in one of the rooms, I get to pay the whole cost of m3.

The remaining cost => Total Bill - (Cost of all three AC) is divided amongst five people and added to give the final amount each of has to pay.
```

<h2>Pre-defined functionalities</h2>
<ul>
<li>Five roomates and their names</li>
<li>m1 divided between first two roomates.</li>
<li>m2 divides between third and fourth roomates</li>
<li>m3 taken up fully by the fifth roomate</li>
<li>Remaining bill divided between all five roomates</li>
</ul>

<h2>File Details</h2>
<ul>
<li>main.py is the main runnable file. Output is a GUI module designed using Tkinter module in python.</li>
<li>function.py is the helper file </li>
</ul>

