import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

## Create a dummy dataframe that uses times
dataframe = pd.DataFrame({'Time':pd.date_range("2018-11-01", "2018-11-04", freq="1H")})
dataframe['Value'] = np.random.random(len(dataframe))


## Create figure with matplotlin
fig,ax = plt.subplots(figsize=[8,5])
ax.plot(dataframe['Time'],dataframe['Value'])
ax.set_title("My awesome plot")
ax.set_ylabel("Value")
ax.set_xlim(left=dataframe['Time'].iloc[0])

## Modify the major x-axis to show only days
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d %Y"))
ax.tick_params(axis='x', which='major', length=50, width=0.8)

for label in ax.get_xticklabels(which='major'):
    label.set(ha='left', va='top')

## Modify the minor x-axis to show only hours
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=6))
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%H:%M"))

for label in ax.get_xticklabels(which='minor'):
    label.set(rotation=90, ha='center', va='top',fontsize=8)


## Streamlit layout to display
st.header(":clock130: Plotting dates :clock130: ")
st.write("#### The pandas dataframe")
st.dataframe(dataframe)
st.pyplot(fig)
