# SSA-Satellite-Analysis
An open-source Space Situational Awareness (SSA) program that tracks live satellite data and live space weather data in an interactive dashboard to create a risk assessment for satellites in LEO.

### What is Space Situational Awareness (SSA)?
SSA is any framework that provides for the knowledge of internal or external threats, environmental conditions, or obstructions to assets in space. These assets are oftentimes satellites that serve an integral function for the United States military,
NASA, or private space companies (such as SpaceX's Starlink satellite constellation).

SSA is also a critical function of the United States Space Force, where national security heavily relies upon the operational integrity on a plethora of satellites in Low Earth Orbit (LEO). Many complex programs exist to track this operational integrity
that are used by the U.S Space Force and many other government and private entities. However, the goal of this project is to demonstrate the ease and simplicity of creating a lighter-duty SSA dashboard that is also open-source since most SSA dashboards are closed-source.

### A Brief Overview of this Project
This project gathers satellite and space debris data from Celestrak and space weather data from NOAA and uses python to propagate that data in real time 
based on orbital mechanics principles. The "back-end" of this project deals with wrangling this large amount of data and feeding it to the "front-end" in an accessible format.

The front-end consists of a simple dashboard which displays the live positions of satellites and debris and also gives data for solar flares, geomagnetic storms, and proton flux etc.
This data is fed into an algorithm that outputs a unique "risk factor" for each satellite. This risk factor is dependent upon the satellite's proximity to other spacecraft, space debris,
and the general conditions of the space environment at a given time.

In a nutshell, this project demonstrates the ability to create a simple-to-use, light-weight, open-source live satellite tracking program that is useful whether you're stargazing, trying to 
catch a glimpse of the ISS, or assessing satellite operational integrity.