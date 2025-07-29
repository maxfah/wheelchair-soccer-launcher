# Assembly Guide

This guide provides detailed, step-by-step instructions for fabricating and assembling all components of the wheelchair soccer launcher.

![Aseembled Wheelchair Soccer Launcher](/images/wheelchair-soccer-launcher-side.png)

### **Table of Contents**

1. **[Before You Begin](#before-you-begin)**  
2. **[Cart Assembly](#cart-assembly)**  
3. **[3D Print Fabrication](#3d-print-fabrication)**
4. **[Electronics Assembly](#electronics-assembly)**  
5. **[Raspberry Pi Pico Programming](#raspberry-pi-pico-programming)**
6. **[Mechanical Assembly](#mechanical-assembly)**

## Before You Begin

This section outlines all the tools and parts you'll need to gather before starting the build.

### Bill of Materials (BOM)

A complete list of all project components and their purchase links can be found using the links below.

* **[bill-of-materials.md](/bill-of-materials.md)**
* **[bill-of-materials.xlsx](/bill-of-materials.xlsx)**

### Tool List

| Tool | Specifications | Notes |
| :---- | :---- | :---- |
| Screwdriver | 3mm phillips head | For various assembly tasks |
| 3D Printer | Minimum 256x256x256mm build volume | To fabricate the custom parts |
| Hand Tap | 5mm tap size | For creating threads in plastic |
| Saw | \- | For cutting wood dowels and PVC pipe |
| PVC Pipe Cutter | \- | A saw will work, but a cutter is easier |
| Soldering Iron | \- | For electronics assembly |
| Tape Measure | \- | For measurements |
| Dial Caliper | \- | For precise measurements |
| Superglue | \- | For permanently bonding small parts |
| Micro USB cable | \- | For programming Raspberry Pi Pico |
| Heat Gun | \- | For wire heat shrink |
| Hex Keys | 1.5mm, 2.5mm, 3mm size | For socket head screws |
| Wire Tools | Wire Stripper, Wire Cutter, Hand Crimper | For all electronics wiring. |
| Hand drill | 1/8", 5/32”, 3/8" drill bit | For drilling holes in PVC and wood. |
| Wrenches | \- | For tightening M5, M6, and 3/8" nuts and bolts. |

## Cart Assembly

This section details how to build the PVC cart that attaches to the wheelchair and funnels the ball to the launcher.

![Assembled PVC Cart](/images/full-cart-assembly.png)

### Step 1: Cut PVC Pipes

Using a saw or PVC pipe cutter, cut the 3/4" PVC pipe into the following lengths:

| Length | Quantity |
| :---- | :---- |
| 36” | 2 |
| 20” | 2 |
| 11” | 4 |
| 5” | 1 |
| 2” | 23 |

### Step 2: Assemble the Main Frame

Gather the PVC Tee and 90° Elbow fittings and the cut pipe sections. Assemble the four sub-frames as shown in the diagram below.

![Main Cart Frame Design](/images/main-cart-frame-design.png)
*Design mockup created using [Crafty Amigo](https://www.craftyamigo.com/)*

| Part Description | Central Frame | Left Frame | Right Frame | Back Frame | Total |
| :---- | ----- | ----- | ----- | ----- | ----- |
| 3/4" Tee PVC | 7 | 3 | 3 | 1 | 14 |
| 3/4" 90° Elbow PVC | 0 | 4 | 4 | 2 | 10 |
| 3/4" x 2" Tube PVC  | 6 | 6 | 6 | 2 | 20 |
| 3/4" x 11" Tube PVC  | 0 | 2 | 2 | 0 | 4 |
| 3/4" x 20" Tube PVC  | 2 | 0 | 0 | 0 | 2 |
| 3/4" x 5" Tube PVC  | 1 | 0 | 0 | 0 | 1 |

**Assembly Notes:**

* **Dry Fit First:** Assemble the entire cart without glue first to ensure all parts fit correctly.  
* **Angles:** The Tee fitting on the Central Frame that connects to the Back Frame should be parallel to the ground. The Left and Right frames should extend out from the Central Frame at a 45-degree angle.  
* **Glue Later:** Once you have confirmed the fit, disassemble, apply PVC primer and cement, and reassemble each joint for a permanent bond. 

### Step 3: Create the Three Cart Wheels

This step covers creating and attaching the three caster wheels to the Left, Right, and Back Cart Frames.

![Cart Wheel](/images/cart-wheel.png)

1. Cut three 1-inch pieces from the **3/4" Wood Dowel**.  
2. Center one dowel piece inside a **PVC Cap** and drill a 3/8" hole through the cap and the dowel.  
3. Insert the threaded stem of a caster wheel through the hole in the PVC cap and dowel.  
4. On the inside of the cap, place a **3/8" Flat Washer** over the threaded stem and secure it with a **3/8" Hex Nut.**  
5. Insert one of the remaining **3/4" x 2" PVC Pipes** into the cap.  
6. Repeat this process for all three wheels.  
7. Connect the assembled cart wheels to the designated open PVC tees on the Right, Left, and Back frames. 

### Step 4: Attach the Aluminum Extrusion

![Aluminum Extrusion](/images/aluminum-extrusion-pvc-connection.png)

1. Drill a hole on both sides of the back frame’s elbow joint and the center frame’s horizontal tee joint. The holes should be parallel to the ground, 0.4" from the edge, and drilled with a 5/32” bit.  
2. Use a 5mm hand tap to thread each hole.  
3. Screw an **M5 x 10mm Screw** into each hole and attach a **T-Nut** to the inside, leaving it loose.  
4. Align the T-nuts and slide the aluminum extrusion into both joints, then tighten the screws completely.

### Step 5: Create the Two Wheelchair Grips

![Wheelchair Grip](/images/wheelchair-grip.png)

1. Take two **QUICK FIST Mini Clamps**.  
2. Slide an **M6 x 30mm Bolt** completely through one clamp, with the bolt head on the clamp's interior.  
3. Place three **M6 Flat Washers** on the end of the bolt.  
4. Slide the bolt through the back of the second QUICK FIST Mini Clamp.  
5. Secure the assembly with a **Nylon Lock Nut**, tightening it enough to allow the clamps to turn with some resistance.  
6. Repeat this process for the second grip

### Step 6: Attach the Two Wheelchair Arms

![Cart Arm](/images/cart-arm.png)

1. Take the two **3/4" x 36” PVC Pipes** and position one end of each on top of and perpendicular to the **20” PVC Pipes** on the center frame.  
2. At each intersection, use a **Cross Connector Pipe Clip** to join the pipes. The nuts should be tight enough to prevent side-to-side movement but still allow for rotation.  
3. Attach one of the previously assembled Mini Clamp grips to the other end of each 36” PVC pipe.

### Final Cart Assembly

![Assembled PVC Cart](/images/full-cart-assembly.png)

## 3D Print Fabrication

This section details how to print and prepare the custom components for the launcher assembly. Component names used here correspond to the `.step` filenames. The parts were designed in Fusion 360, and the `.f3d` file is available for modifications.

![3D Printed Components](/images/3d-printed-components.png)

### Step 1: Print Each component

First, download the design files from the [3D Models](/3d-models/) folder. Files are available in `.step`, `.f3d`, `.3mf`, and individual `.stl` formats.

**Recommended Print Settings**

| Setting | Value |
| :---- | :---- |
| Printer | Bambu Lab P1S |
| Resolution | 0.2mm |
| Supports | Yes |
| Rafts | No |
| Infill Pattern | Gyroid |
| Filament | SUNLU PLA+ 2.0 |

**Part-Specific Settings**

Use the following infill percentages for different components (the specific Bambu presets are also noted).

| Parts | Infill | Slicer Preset |
| :---- | :---- | :---- |
| Band Anchor, Casing, Plunger, Plunger Spring Lock | 40% | 0.2mm Bambu Strength Preset |
| All Other Components | 15% | 0.2mm Bambu Standard Preset |

**Note:** It's recommended to lower the print speed when printing the Casing due to the thin walls

### Step 2: Tap M5 holes

For reliable connections, you'll need to tap threads into several of the printed parts. First, pre-drill each hole with the 5/32” drill bit, then create threads using a 5mm hand tap.

**Launcher Base**:

![Launcher Base Drill Locations](/images/launcher-base-drill-locations.png)

* Drill and tap the middle **3 holes** completely through the bottom.  
* Drill and tap the front **2 holes** to a depth of 3/4" (do not drill through).

**Electronics Base & Launcher Base**:

![Electronics Base Drill Locations](/images/electronics-base-drill-locations.png)

* Drill and tap **2 holes** on either side through both parts to a depth of 0.3". Do not go entirely through the launcher base.

**Launcher Base & Battery Case**:

![Battery Case Drill Locations](/images/battery-case-drill-locations.png)

* Drill and tap **4 holes** at each corner through both parts to a depth of 0.75".

**Casing & Launcher Base**:

![Casing Drill Locations](/images/casing-drill-locations.png)

* Drill and tap **4 holes** at each lower corner through both parts to a depth of 0.3". Do not go entirely through the launcher base.

### Step 3: Break in Components

Some parts require a "break-in" to ensure smooth operation. Manually move the following components back and forth to reduce friction.

![Breaking in Plunger](/images/breaking-in-plunger.png)

* Ensure the **Plunger** can slide freely within the launcher base.

![Breaking in Axles](/images/breaking-in-axles.png)

* Check that the **Pawl Axle** (black) can rotate freely in its hole in the launcher base.  
* Confirm the **Band Anchor** (white) fits properly into its slot in the launcher base.

![Breaking in Hex Axle](/images/breaking-in-hex-axle.png)

* Check the **5mm Hex Axle** can rotate freely in its hole in the launcher base.

![Breaking in Gears](/images/breaking-in-gears.png)

* Make sure the **Gears** can slide along the 5mm Hex Axle. This should require some force and not be loose

3. ## Electronics Assembly

This section details how to assemble, mount, and wire the electronic components. For clarity, follow the wiring diagram and pictures provided. It's helpful to imagine the final placement of the components to cut wires to a suitable length—not too short to be taut, but not so long they become tangled.

### Step 1: Prepare the Main Control Board

This step focuses on mounting the L298N Motor Driver and Raspberry Pi Pico to the PCB, creating the central control unit. 

![Main Control Board](/images/main-control-board.png)

***Please Note:** Ignore the wires in the picture, they will be added later.*

1. **Mount Standoffs to L298N**: Screw the four **M3 x 15mm Double-Pass Standoffs** into the corners of the **L298N Motor Driver** using four **M3 x 12mm Standoff Screws**.  
2. **Position on PCB**: Place the L298N assembly onto the **5cm x 7cm PCB Board**. The L298N's heat sink should face one edge of the board.  
3. **Drill Mounting Holes**: Mark and drill four holes with a **1/8" drill bit** where the standoffs will connect to the PCB. Two of these holes should be corner holes. Ensure these corner holes align with the mounting holes on the  
    **3D Printed Electronics Base**. Drill holes in the other two corners of the PCB as well.  
4. **Secure L298N**: Fasten the L298N to the PCB by screwing two **M3 x 6mm screws** through the board and into the two non-corner standoffs. The corner holes will be used later to mount the entire board.  
5. **Place Raspberry Pi Pico**: Insert the **Raspberry Pi Pico** into the PCB so its micro-USB port faces the edge opposite the L298N motor driver.

### Step 2: Mount the Motor

![Mounting Motor](/images/mounting-motor.png)

1. Attach the **DC Motor** to the **Motor Mounting Bracket**.  
2. Place the motor and bracket onto the **3D Printed Electronics Base**. The motor shaft should face the right (the two clip arms facing back).  
3. Secure the assembly by inserting four **M5 x 12mm screws** up through the bottom of the electronics base and into the bracket. Tighten with four **M5 nuts**.

### Step 3: Mount the Limit Switch

![Mounting Limit Switch](/images/mounting-limit-switch.png)
   
***Please Note:** Ignore the wires in the picture, they will be added later.*

1. Position the **Limit Switch** on the back of the **3D Printed Launcher Base**.  
2. Use a zip tie fed through the two small holes to secure the switch. The zip tie should sit flush inside the outer wall of the print.  
3. Cut the excess zip tie.

### Step 4: Assemble the Launch Button

This step covers building the external launch button.

![Launch Button Electronics](/images/launch-button-electronics.png)

1. **Place Components**:  
   1. Insert a **6x6x9.5mm Tactile Push Button** into the center of the **3D Printed Launch Button Base**.  
   2. Place a **3.5mm Female Mount Jack** through the hole in the side of the base.  
2. **Solder Internal Wires**: Solder two short wires to connect the bottom and left pins of the female jack to the two pins on the tactile button.

![Launch Button Cable](/images/launch-button-cable.png)

3. **Prepare the Cable**: Solder a **3.5mm Male Plug** to each end of the **11-foot 3-Conductor Wire**. You only need to connect the red-to-red and black-to-black wires. Use 4mm heat shrink on the individual connections and 6mm heat shrink over the entire cable end.

![Launch Button](/images/launch-button.png)

4. **Final Button Assembly**:  
   1. Place the **3D Printed Launch Button Top** over the tactile button and press down to snap it in place.  
   2. Apply super glue around the edge of the female jack and push it firmly into its hole.  
   3. Apply super glue around the top edge of the button base and press the **3D Printed Launch Button Case** on top, aligning the rounded portion with the female jack.

### Step 5: Wire the L298N Components

![Wiring L298N](/images/wiring-l298n.png)
![Launcher Circuit](/images/launcher-circuit.png)
*Circuit image created using [Cirkit Designer](https://www.cirkitstudio.com/)*

***Note on Wire Lengths:** For the best fit, orient the L298N/PCB board in its final position—mounted in front of the motor with the heat sink facing right. The approximate lengths provided in the following steps are based on this layout.*

1. **Motor to L298N**:  
   1. Solder a \~2.3" wire from **OUT3** on the L298N to the left pin of the DC motor.  
   2. Solder a \~3.8" wire from **OUT4** on the L298N to the right pin of the motor.  
2. **L298N to Pico (Signal)**:  
   1. Crimp female pin connectors onto two \~2.5" wires and insert them into a **2-Pin Housing Connector**.  
   2. Solder the wire from **IN3** on the L298N to **Pin 1** of the Pico.  
   3. Solder the wire from **IN4** on the L298N to **Pin 2** of the Pico.  
3. **Power Switch to Components**:  
   1. On the **On/Off Switch**, connect the red wire from the **NO** terminal to the **12V** terminal on the L298N. Connect the black wire to the **GND** terminal.  
   2. Connect the red and black wires from the **COM** terminal to the **\+** and **\-** terminals, respectively, of the **5.5mm Female DC Barrel Jack**.  
   3. Zip tie the unused **NC** wire to the **COM** and cut excess  
4. **L298N to Pico (Power)**:  
   1. Connect a \~1.5" wire from the **5V** terminal on the L298N to **Pin 39** on the Pico.  
   2. Connect a \~1.5" wire from the L298N's **GND** terminal to **Pin 38** on the Pico.

### 

### Step 6: Wire the Casing Components

![Wiring Casing](/images/wiring-casing.png)
![Launcher Circuit](/images/launcher-circuit.png)

This step prepares the **connector cable** for the components that will be mounted in the outer casing.

***Wiring Note:** To easily orient the connector, use distinctly colored wires. This guide will refer to the wires by number based on the picture: Wire 1 (Red), Wire 2 (Black), and Wires 3-5 (Yellow).*

1. **Mount Jack**: Insert the **3.5mm Female Mount Jack** into the front-most hole of the 3D printed casing and secure it with its nut.  
2. **Prepare Reset Button**: Insert a **6x6x11mm Tactile Push Button Switch** into the **Off Button Bottom**, then press the **Off Button Top** onto it.  
3. **Create Connector Cable**:  
   1. Cut seven \~6.5" wires and one \~1.5" wire.  
   2. Crimp female pin connectors onto four of the long wires and the one short wire. Insert these five wires into a **5-Pin Housing Connector**.  
   3. Solder the short wire to the three remaining long wires to create a shared connection.  
4. **Solder Components to the Connector Cable**:  
   1. **RGB LED**: Solder the longest pin (Pin 2\) to the black wire (wire 2). Solder the red pin (Pin 1\) to the 470 Ω resistor, and then solder one of the shared red wires (wire 1\) to the other end of the resistor. Solder the green pin (Pin 3\) to the first yellow wire (wire 3). Cut the blue pin (Pin 4).  
   2. **Reset Button**: Solder another shared red wire (wire 1\) to one pin of the button and the second yellow wire (wire 4\) to the other pin.  
   3. **Mount Jack**: Solder the last shared red wire (wire 1\) to the bottom pin and the last yellow wire (wire 5\) to the left pin.  
5. **Finalize Casing**: Press-fit the 5mm LED and the Reset Button into their holes in the casing. Zip tie the connector cable wires together neatly.

### Step 7: Wire Raspberry Pi Pico Components

This final wiring step connects the limit switch and the casing's connector cable to the main control board.

![Wiring Pico](/images/wiring-pico.png)
![Launcher Circuit](/images/launcher-circuit.png)

***Please Note:** Disregard the soldering mistake in the photo where the yellow wire for Pin 4 is on the edge of the board. Ensure this wire follows the pattern of the others.*

1. **Limit Switch to Pico**:  
   1. Solder two \~10" wires to the **COM** and **NO** pins of the limit switch.  
   2. Route these wires through the channel in the launcher base.  
   3. Solder the **COM** wire to **Pin 36** of the Pico and the **NO** wire to **Pin 7**.  
2. **Casing's Connector Cable to Pico**:  
   1. Create a male-ended connector by cutting five \~5" wires that match the colors of your female connector. Crimp **Male Pin Connectors** onto them and insert them into a **5-Pin Male Housing Connector** in the same color order.  
   2. Solder the wires from the male connector to the Pico as follows: the red wire (1) to **Pin 36**, the black wire (2) to **Pin 3**, the first yellow wire (3) to **Pin 4**, the second yellow wire (4) to **Pin 5**, and the last yellow wire (5) to **Pin 6**.  
   3. Zip tie the wires together neatly.

## Raspberry Pi Pico Programming

### Step 1: Setup MicroPython on the Pico

First, you'll install MicroPython, the programming language used for this project. The easiest way to do this is with the Thonny IDE. Detailed instructions can be found [here](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/1).

1. **Download Firmware:** Download the official MicroPython UF2 file for the Raspberry Pi Pico from the [Raspberry Pi documentation page](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).  
2. **Enter Bootloader Mode:** Unplug your Pico. Press and hold the **BOOTSEL** button on the Pico, and while holding it, plug the Pico into your computer's USB port.  
3. **Copy Firmware:** Release the BOOTSEL button. The Pico will appear as a removable drive named `RPI-RP2`. Drag and drop the `.uf2` file you just downloaded onto this drive. The Pico will automatically reboot.  
4. **Install Thonny:** If you don't have it, download and install [Thonny](https://thonny.org/), a beginner-friendly Python IDE.  
5. **Configure Thonny:** Open Thonny. Go to `Tools > Options` and select the `Interpreter` tab. From the interpreter dropdown, choose **MicroPython (Raspberry Pi Pico)**. The port should be detected automatically. Click `OK`.

### Step 2: Load the Launcher Program

Now you'll copy the project's code onto the Pico.

1. **View the Raw Code:**  
   1. Navigate to the [`main.py`](/micropython-code/main.py) file in the GitHub `micropython-code` folder.  
   2. In the top-right corner of the file view, click the **`Raw`** button. This will open a new browser tab showing only the plain text of the code.  
2. **Copy the Code:**  
   1. Select all the text on the page (you can use `Ctrl+A` on Windows or `Cmd+A` on Mac).  
   2. Copy the selected text to your clipboard (`Ctrl+C` or `Cmd+C`).  
3. **Paste and Save in Thonny:**  
   1. Go back to Thonny and open a new, blank file.  
   2. Paste the code you copied into Thonny's editor (`Ctrl+V` or `Cmd+V`).  
   3. Go to `File > Save copy`. When prompted where to save, select **Raspberry Pi Pico**.  
   4. Name the file exactly **`main.py`** and click `OK`. This is critical, as the Pico is programmed to run this file automatically on startup.

### Step 3: Final Assembly and Testing

This final check verifies that all connections and code are working correctly.

![Testing Electronics](/images/testing-electronics.png)

1. **Make Connections:**  
   1. Connect the 5-pin **connector cable** from the main casing to the corresponding 5-pin connector on the electronics board.  
   2. Plug one end of the **launch button cable** into the 3.5mm jack on the casing and the other end into the launch button itself.  
   3. Insert three charged **18650 batteries** into the battery case holder and plug its barrel jack into the power port.  
2. **Perform Functional Test:**  
   1. Turn the main power switch to ON.  
      1. **Expected Result:** The LED should turn **green**, and the motor should begin to rotate.  
   2. Press the limit switch on the launcher base.  
      1. **Expected Result:** The motor should **stop**.  
   3. Press the external launch button.  
      1. **Expected Result:** The motor should **rotate again**.  
   4. Press the limit switch again.  
      1. **Expected Result:** The motor should **stop**.  
   5. Press the off button on the casing.  
      1. **Expected Result:** The motor should rotate for half a second, then stop, and the LED should turn **red**.

## Mechanical Assembly

This section details the final assembly of the launcher mechanism and its attachment to the cart.

### Step 1: Attach Launcher Base to Cart

![Launcher Base Bottom](/images/launcher-base-bottom.png)

1. **Prepare the Launcher Base**: Insert three **M5 x 25mm Bolts** with **M5 Flat Washers** through the three center holes on the bottom of the **3D Printed Launcher Base**.  
2. **Attach Spacer and T-Nuts**: From underneath, slide the **3D Printed Bottom Spacer** over the bolts. Loosely thread on three **M5 T-Nuts**.

![Attaching Launcher Base to Cart](/images/attaching-launcher-base-to-cart.png)

3. **Mount to Cart**: Temporarily remove the back frame of the PVC cart. Slide the T-Nuts of the launcher assembly into the channel of the aluminum extrusion. Position the assembly as far forward as it can go, until the PVC frame stops it.  
4. **Secure Launcher**: Firmly tighten the three M5 bolts until the launcher base is secure and cannot move.  
5. **Re-attach Back Frame**: Re-install the back frame of the cart, adjusting the T-nuts as needed to fit.

### Step 2: Install the Plunger

![Assembled Plunger](/images/assembled-plunger.png)

1. **Prep the Plunger**: Slide the **Plunger Lock** halfway through the side of the **Plunger**. Hook both **Extension Springs** onto the lock, ensuring they face the same direction. Slide the lock the rest of the way through until it is flush on both sides.

![Launcher Base with Plunger](/images/launcher-base-with-plunger.png)

2. **Insert into Launcher**: Place the plunger assembly into the launcher base. Secure the other end of the springs onto the two vertical poles inside the launcher base.

### Step 3: Mount the Electronics.

![Mounted Electronics Base](/images/mounted-electronics-base.png)

1. **Attach Electronics Base**:  
   1. Insert four **M3 x 12mm Standoff Screws** with **M3 Washers** up through the bottom of the **3D Printed Electronics Base**.  
   2. Snap the electronics base onto the launcher base.  
   3. Secure the front with two **M5 x 30mm Bolts** and **M5 Washers**. Do not overtighten, as the plunger must still slide smoothly.  
   4. Secure the sides with two **M5 x 8mm Screws**.

![Mounted Control Board](/images/mounted-control-board.png)

2. **Mount Control Board**:  
   1. Screw two **M3 (15mm) Double-Pass Standoffs** onto the two holes near the front of the motor. On the other side, screw in two **M3 (15mm \+ 6mm) Single-Head Standoffs**.  
   2. Fasten the **Main Control Board** onto the two single-head standoffs (this should be the side with the L298N heat sink).  
   3. Secure the other side of the board using two **M3 x 6mm Standoff Screws** on the open double-pass standoffs.

![Assembled Motor Gear](/images/assembled-motor-gear.png)
![Mounted Motor Gear](/images/mounted-motor-gear.png)

3. **Assemble and Mount Motor Gear**:  
   1. Take one of the **3D Printed Full Gears**. Through the recessed side, insert four **M3 x 14mm Socket Head Screws**.  
   2. Fully tighten four **M3 Standoff Nuts** onto the screws.  
   3. Place a **6mm Flange Coupler** (flange facing the gear) over the nuts and secure it with four **M3 Coupler Nuts**.  
   4. Attach the entire gear assembly to the motor shaft, ensuring the gear sits flat against the launcher base wall.  
   5. Lock the coupler onto the flat part of the motor axle with an **M3 Coupler Fastening Screw**.

### Step 4: Install Axles and Battery Case

![Mounted Hex Shaft](/images/mounted-hex-shaft.png)

1. **Assemble Hex Shaft**:  
   1. Insert the **5mm x 135mm Hex Shaft** through the front-most hole in the launcher base.  
   2. From one side, slide on the components in this order: **Spacer**, **Half Gear**, **Long Spacer**, **Half Gear**, **Spacer**. Make sure the half gears have the same orientation.  
   3. Center the shaft so it is even on both sides.  
   4. Attach the other **Full Gear** to one end of the shaft so it meshes with the motor gear.  
   5. Secure both ends of the hex shaft with a **Flange Coupler** and an **M3 Coupler Fastening Screw**.

![Mounted Pawl](/images/mounted-pawl.png)

2. **Install Pawl**:  
   1. Slide the **3D Printed Pawl Axle** through the upper hole in the launcher base and through the **Pawl**.  
   2. Wrap a rubber band through the designated holes on the pawl and secure it to the **Band Anchor**, which is inserted through the lower launcher base hole.

![Mounted Battery Case](/images/mounted-battery-case.png)
![Mounted Batteries](/images/mounted-batteries.png)

3. **Mount Battery Case**:  
   1. Attach the **3D Printed Battery Case** to the upper four holes of the launcher base using four **M5 x 14mm Screws**, with the wire port facing the electronics.  
   2. Insert the **18650 Battery Holder** (with three charged batteries) into the printed case.  
   3. Plug the battery holder's barrel jack into the female connector attached to the power switch.

### Step 5: Attach the Launcher Casing

![Attached Casing](/images/attached-casing.png)

1. **Disassemble for Fitting**: Temporarily unscrew the two screws holding the aluminum extrusion and slide it off the cart's center frame.  
2. **Fit the Casing**: Gently fit the **3D Printed Casing** over the entire launcher assembly, being careful not to pinch any wires.  
3. **Connect Electronics:** Plug the 5-pin male connector from the main control board into the 5-pin female connector attached to the casing's wiring.  
4. **Secure Casing**: Fasten the casing to the launcher base using four **M5 x 8mm Screws** in the bottom corners.  
5. **Reassemble**: Guide the aluminum extrusion back onto the center frame, adjusting the T-nuts as needed, and tighten the screws to secure it to the PVC cart.

## Final Assembly

![Final Assembly 1](/images/wheelchair-soccer-launcher-front.png)
![Final Assembly 2](/images/wheelchair-soccer-launcher-side.png)

