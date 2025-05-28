---
weight: 1
author: ---
---

# Neuclear Reactions Rates and Core Boundary Mixing on the Seismology of Red Clump Stars

## Introduction

In this lab we will investigate the influence of core boundary mixing, neuclear
reaction rates and metallicity on the period spacing of Red Clump (RC) stars.
This lab if following this paper - [Noll et al. 2024](https://www.aanda.org/articles/aa/abs/2024/03/aa48276-23/aa48276-23.html).

Red clump stars are core-helium burning stars with initial masses around 0.8–2.0 $M_{\odot}$, located in a narrow region of the color-magnitude diagram
following the helium flash.

Stars in the red clump (RC) phase are burning helium in their cores after
undergoing the helium flash. These stars are of low mass and typically have
degenerate helium cores at the tip of the red giant branch. The helium ignition
lifts this degeneracy and establishes a stable helium-burning core, surrounded
by a hydrogen-burning shell.

In the following Figure you see an Hertzsprung–Russell (HR) diagram of the GALAH DR2 sample. The highlighted rectangle marks the red clump stars region, which aligns with the highest stellar number-density contours after RGB bump just below. The color scale is linear, where darker shades indicates higher stellar densities. The Figure is taken from [Kumar et al. 2020](https://www.nature.com/articles/s41550-020-1139-7).
![HR diagram RC](/thursday/RC_HR_daiagram.png)

Several physical processes in red clump stars remain uncertain. A key uncertainty is **core boundary mixing (CBM)** — whether semiconvection or overshooting dominates
near the convective core edge and which mixing schemes can support the stars we later observe. Another major uncertainty involves the nuclear reaction rates during helium burning.
The nuclear reaction rates are temperature dependent and different rates can produce a different internal stellar structure.

Asteroseismology enables us to study the internal structure of these stars through their oscillation modes. In particular, mixed modes—which behave like gravity modes in the core and pressure modes in the envelope—are highly sensitive to the structure near the convective core boundary. The asymptotic period spacing $\'(\Delta \Pi\)'$ of dipole mixed modes serves as a probe of the size and composition gradient in the helium-burning core. Hence, the period spacing in RC stars as a result from different physical prescriptions in MESA gives us theoretical predictions to compare with observations and constrain their stellar structure.

**Maxilab1**: We will learn about different mixing schemes and test their affect on the period spacing $'\(\Delta \Pi\)'$ in the core He burning phase.

**Maxilab2**: We will test how different nuclear reaction rates influence the period spacing $'\(\Delta \Pi\)'$ in the core He burning phase.

**Warning!** These MESA labs have been built in low time and spatial resolution (including some missing physics, like using the most basic nuclear network net and no mass loss) so the students will be able to get results within a few minutes.


## Maxilab1: Diffetent Mixing Schemes

## Maxilab2: Different Reaction Rates
### Background:

During the core helium-burning (CHeB) phase, the energy production of the star is primarily driven by two nuclear reactions:

- The **triple-alpha process** ($'\(3\alpha\)'$): three helium nuclei ($'\(^4\mathrm{He}\)'$) fuse to form carbon ($'\(^{12}\mathrm{C}\)'$). It occurs in two steps: $^4\mathrm{He} + {}^4\mathrm{He} \rightarrow {}^8\mathrm{Be}$ and ${}^8\mathrm{Be} + {}^4\mathrm{He} \rightarrow {}^{12}\mathrm{C} + \gamma$.
- The **$'\(^{12}\mathrm{C}(\alpha, \gamma)^{16}\mathrm{O}\)'$** reaction: a carbon nucleus captures an alpha particle to form oxygen (${}^{12}\mathrm{C} + {}^4\mathrm{He} \rightarrow {}^{16}\mathrm{O} + \gamma$).

As was mentioned in the introduction to the Maxilab, nuclear reaction rates and their
dependence on temperature are uncertainty in RC evolution, leading to different
stellar interior and different period spacing to compare with observations.
Helium burning in RC stars is driven primarily by two nuclear reactions.
The $'\(3\alpha\)'$ process dominates during the early stages of the core
helium-burning phase, while the $'\(^{12}\mathrm{C}(\alpha, \gamma)^{16}\mathrm{O}\)'$ reaction becomes more important later on.

These reactions are highly temperature-sensitive and uncertain, especially the $'\(^{12}\mathrm{C}(\alpha, \gamma)^{16}\mathrm{O}\)'$ rate, which occurs at low energies in stellar interiors and cannot be measured directly under such conditions. Instead, it must be extrapolated from higher-energy laboratory data, which are expected to different from the low-energy conditions where the reaction occurs in, in RC stars.

Changes in these rates affect the core composition, the duration of the core He burning
(CHeB) phase, and indirectly the size and structure of the convective core.
This, in turn, influences the period spacing $'\(\Delta \Pi\)'$, making reaction rates a key variable to explore.

In this Maxilab2, we will learn to change the reaction rates in MESA and we will reproduce together as a class Figure 5 and Figure 6 from [Noll et al. 2024](https://www.aanda.org/articles/aa/abs/2024/03/aa48276-23/aa48276-23.html), where each table will explore different initial stellar mass and reaction rate.

Figure 5 from [Noll et al. 2024](https://www.aanda.org/articles/aa/abs/2024/03/aa48276-23/aa48276-23.html). Showing the evolution of $'\(\Delta \Pi\)'$ during the CHeB phase for different $\(3\alpha\)$ reaction rates as a function of the CHeB age (top panel) and central helium abundance (lower panel).
![Figure 5 from Noll et al. 2024](/thursday/aa48276-23-fig5.jpg)

Same as Figure 5 for different $'\(\,^{12}\mathrm{C}(\alpha, \gamma)^{16}\mathrm{O}\)'$ reaction rates:
![Figure 6 from Noll et al. 2024](/thursday/aa48276-23-fig6.jpg)

### Aims
**MESA aims**: In this Maxilab you will learn how find and change the nuclear reaction net, how to read the nuclear reaction net files and where to find it in the $MESA_DIR. You will learn how to change reaction rates for specifi profiles and how to incorporate all of that in your MESA inlist.

**Science aims**: You will learn how changing the reaction rate for a specific evolution phase in stellar evolution chnages the composition and inner structure and hence the period spacing pattern.

**Solution**: In case you get stuck at any point during the exercises, you can find the solution to this Maxilab [here](https://github.com/noi26/MESA_summer_school-maxilab2-Day4/blob/main/maxilab2_solution.zip). Clicking this link will download a zipped directory named: maxilab2_solution.zip.

### Setting up the MESA model
In this Maxilab we will fix the mixing scheme on maximal overshooting to test the reaction rates affect on the period spacing.

If you ran your MESA models in Maxilab1 using the maximal overshooting scheme - you can copy this work directory and continue the Maxilab with it. If you used another mixing scheme, or if you are not sure about your solution - please download the correct model from [here](https://github.com/noi26/MESA_summer_school-maxilab2-Day4/blob/main/maxilab2.zip) - it will download a work directory named maxilab2.zip.

If you want to unzip the folder using the terminal, you can use:
```linux
unzip maxilab2.zip
```

**Terminal commands**:

```linux
cd 1M_Z002_maximal_overshooting
./clean && ./mk
```

Make sure that you manage to compile and start the run without any issues and break the run after you see pgplot.

{{< details title="Task 1" closed="false" >}}
Go over the inlist_project file. Make sure that maximal overshooting is indeed the mixing scheme that is set.
{{< /details >}}

{{< details title="Hint 1" closed="true" >}}
There are different mixing scheme inside the solution to Maxilab1 that you downloaded. there are comments explaining each, and there is one for the maximal overshooting scheme.
Make sure that the rest of the mixing schemes are all commented out besides the maximal overshooting one.
{{< /details >}}

{{< details title="Task 2" closed="false" >}}
- If not changing the nuclear reaction net, then MESA will run with the default one. Find the name of this net.
- Find the file of this nuclear reaction net and find the names of the reaction rate files matches the He burning processes.
{{< /details >}}

{{< details title="Hint 2" closed="true" >}}
- You can find the nuclear reaction net options under &star_job variables.
- You can find the nuclear reaction net file in you local MESA directory. Be carful not to change anything in this file, since MESA reads it every time it runs with this net (you can copy it to prevent issues).
- To find the name of the reaction rate files that are related to He burning processes - look the two closest to the $'\(3\alpha\)'$ and $'\(\,^{12}\mathrm{C}(\alpha, \gamma)^{16}\mathrm{O}\)'$.
{{< /details >}}

The names of the reaction rate files you found are leading to files describing the reaction rate of each process as a function of temperature. In the bonus exercise we will direct you where to find these files. If you want to use another file, computed, for example, by a recent study that MESA does not include yet, you can add this files and direct MESA to read them.

{{< details title="Task 3" closed="false" >}}
- Find the variables that need to be changed in order to change the reaction rates for the two He burning processes (also use the names of the files you found in Task 2)
- The reaction rates values we need to to change and compute are the default rates times 0.25, 0.5, 1, 2, 5 for the $'\(3\alpha\)'$ process where the reaction rate of $'\(\,^{12}\mathrm{C}(\alpha, \gamma)^{16}\mathrm{O}\)'$ is set on 1 and the opposite. Each table will get a different value to compute.
{{< /details >}}

{{< details title="Hint 3" closed="true" >}}
You can find the variable names under &star_job.
{{< /details >}}

{{< details title="If you want to make sure your &star_job was changed correctly look here" closed="true" >}}
These are the variables needed to be changed:
```fortran
num_special_rate_factors = 2
reaction_for_special_factor(1) = 'r_he4_he4_he4_to_c12'
reaction_for_special_factor(2) = 'r_c12_ag_o16'
special_rate_factor(1) = 1  ! 0.25, 0.5, 1.00, 2.00, 5.00
special_rate_factor(2) = 5   ! 0.25, 0.5, 1.00, 2.00, 5.00
```
In this example the $'\(3\alpha\)'$ reaction rate (r_he4_he4_he4_to_c12) is set to 1 and the $'\(\,^{12}\mathrm{C}(\alpha, \gamma)^{16}\mathrm{O}\)'$  reaction rate is changed to times 5 (r_c12_ag_o16)
{{< /details >}}

Before we turn to run our models, lets make sure what we have in our pgstar plot.
We can add two plots that can give us information about the reaction rates and the temperature change during the run.

{{< details title="Task 4" closed="false" >}}
Replace the kippenhahn diagram and the mixing profile plot you added in Maxilab1, so we will have a more space to add our two new plots, with the following plots:
- The abundance plot of all the elements the nuclear reaction net we are using displayed as mass fraction in log scale as a function of the mass profile of the star.
- The central temperature ($log_{10}(T_c)$) as a function of the central density ($log_{10}(\rho_c)$) in log-log scale.
{{< /details >}}

{{< details title="Hint 4" closed="true" >}}
Look for the correct plot names under the "single panel profile plots" and the "single panel history plots" options.
{{< /details >}}

Now run you models. In the pgplot you will be able to look at the changing abundances of the elements that take part in He burning (mainly He4, Be7, C12 and O16) as the temperature of the star changes.

```linux
cd 1M_Z002_maximal_overshooting
./clean && ./mk
./rn
```

This is how your pgplot suppose to look like:
![pgplot](/thursday/pgplot.png)
