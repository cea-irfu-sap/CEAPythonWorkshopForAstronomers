"""
Solution to AstroPy Breakout
"""

from astropy import coordinates as c
from astropy import time as t
from astropy import units as u
from astropy.table import Table

# read the data table
cat = Table.read("gll_psc_v14.fit")

# select rows that have sufficient flux (note unit conversion is implicit!)
maxflux = 0.5e-10 * u.TeV/u.cm**2/u.s
selected = cat[ cat['Energy_Flux100']  > maxflux ]

# get the RA/Dec cols (you could also use the Gal L/B columns)
RA = selected['RAJ2000']
Dec= selected['DEJ2000']
coord = c.SkyCoord( ra=RA, dec=Dec )

# define the time and location
paris = c.EarthLocation( lat=48.8567*u.deg, lon=2.3508*u.deg )
tonight =  t.Time("2015-04-09 00:00:00", format="iso", scale="utc")

# calculate the horizontal coordinates 
altaz = coord.transform_to( c.AltAz( obstime=tonight, location=paris ))

# select rows that are visible above 10 deg altitude
visible = selected[ altaz.alt > 10*u.deg ]

# write those rows to a html file
visible.write("visible.html")

# or try an interactive viewer (here I show only 2 columns to make it
# simpler)
visible['Source_Name','ASSOC1','Energy_Flux100']\
    .show_in_browser( jsviewer=True )

# print it to screen too
print "there are {0} bright Fermi objects visible tonight".format(len(visible))
print visible['Source_Name','ASSOC1','Energy_Flux100']