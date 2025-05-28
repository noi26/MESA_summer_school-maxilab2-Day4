import mesa_reader as mr
import matplotlib.pyplot as plt

# make a MesaData object from a history file
h_025_3alpha = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_025_3alpha/history.data')
h_05_3alpha = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_05_3alpha/history.data')
h_1_3alpha = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_1_3alpha/history.data')
h_2_3alpha = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_2_3alpha/history.data')
h_5_3alpha = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_5_3alpha/history.data')

# extract the star_age column of data
ages_025_3alpha = h_025_3alpha.data('star_age')
delta_Pi_025_3alpha = h_025_3alpha.data('delta_Pg')
# extract the star_age column of data
ages_05_3alpha = h_05_3alpha.data('star_age')
delta_Pi_05_3alpha = h_05_3alpha.data('delta_Pg')
# extract the star_age column of data
ages_1_3alpha = h_1_3alpha.data('star_age')
delta_Pi_1_3alpha = h_1_3alpha.data('delta_Pg')
# extract the star_age column of data
ages_2_3alpha = h_2_3alpha.data('star_age')
delta_Pi_2_3alpha = h_2_3alpha.data('delta_Pg')
# extract the star_age column of data
ages_5_3alpha = h_5_3alpha.data('star_age')
delta_Pi_5_3alpha = h_5_3alpha.data('delta_Pg')

# extract the star_age column of data
center_he4_025_3alpha = h_025_3alpha.data('center_he4')
# extract the star_age column of data
center_he4_05_3alpha = h_05_3alpha.data('center_he4')
# extract the star_age column of data
center_he4_1_3alpha = h_1_3alpha.data('center_he4')
# extract the star_age column of data
center_he4_2_3alpha = h_2_3alpha.data('center_he4')
# extract the star_age column of data
center_he4_5_3alpha = h_5_3alpha.data('center_he4')

delta_Pi_cond_025_3alpha = (delta_Pi_025_3alpha != 0) & (center_he4_025_3alpha < 0.9)
delta_Pi_cond_05_3alpha = (delta_Pi_05_3alpha != 0) & (center_he4_05_3alpha < 0.9)
delta_Pi_cond_1_3alpha = (delta_Pi_1_3alpha != 0) & (center_he4_1_3alpha < 0.9)
delta_Pi_cond_2_3alpha = (delta_Pi_2_3alpha != 0) & (center_he4_2_3alpha < 0.9)
delta_Pi_cond_5_3alpha = (delta_Pi_5_3alpha != 0) & (center_he4_5_3alpha < 0.9)

fig, axs = plt.subplots(2, 1, figsize=(6, 8))

ax = axs[0]
ax.plot(ages_025_3alpha[delta_Pi_cond_025_3alpha], delta_Pi_025_3alpha[delta_Pi_cond_025_3alpha], label='0.25_3alpha')
ax.plot(ages_05_3alpha[delta_Pi_cond_05_3alpha], delta_Pi_05_3alpha[delta_Pi_cond_05_3alpha], label='0.5_3alpha')
ax.plot(ages_1_3alpha[delta_Pi_cond_1_3alpha], delta_Pi_1_3alpha[delta_Pi_cond_1_3alpha], label='1_3alpha')
ax.plot(ages_2_3alpha[delta_Pi_cond_2_3alpha], delta_Pi_2_3alpha[delta_Pi_cond_2_3alpha], label='2_3alpha')
ax.plot(ages_5_3alpha[delta_Pi_cond_5_3alpha], delta_Pi_5_3alpha[delta_Pi_cond_5_3alpha], label='5_3alpha')
ax.set_xlabel('age')
ax.set_ylabel('delta_Pg')
plt.legend()

ax = axs[1]
ax.plot(center_he4_025_3alpha[delta_Pi_cond_025_3alpha], delta_Pi_025_3alpha[delta_Pi_cond_025_3alpha], label='0.25_3alpha')
ax.plot(center_he4_05_3alpha[delta_Pi_cond_05_3alpha], delta_Pi_05_3alpha[delta_Pi_cond_05_3alpha], label='0.5_3alpha')
ax.plot(center_he4_1_3alpha[delta_Pi_cond_1_3alpha], delta_Pi_1_3alpha[delta_Pi_cond_1_3alpha], label='1_3alpha')
ax.plot(center_he4_2_3alpha[delta_Pi_cond_2_3alpha], delta_Pi_2_3alpha[delta_Pi_cond_2_3alpha], label='2_3alpha')
ax.plot(center_he4_5_3alpha[delta_Pi_cond_5_3alpha], delta_Pi_5_3alpha[delta_Pi_cond_5_3alpha], label='5_3alpha')
ax.set_xlabel('center_he4')
plt.gca().invert_xaxis()
plt.ylabel('delta_Pg')
plt.legend()
plt.show()



################################################
# make a MesaData object from a history file
h_025_OC = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_025_OC/history.data')
h_05_OC = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_05_OC/history.data')
h_1_OC = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_1_3alpha/history.data')
h_2_OC = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_2_OC/history.data')
h_5_OC = mr.MesaData('/Users/noishitrit/Documents/MESA_runs/MESA_summer_school/maxilab2/LOGS_5_OC/history.data')

# extract the star_age column of data
ages_025_OC = h_025_OC.data('star_age')
delta_Pi_025_OC = h_025_OC.data('delta_Pg')
# extract the star_age column of data
ages_05_OC = h_05_OC.data('star_age')
delta_Pi_05_OC = h_05_OC.data('delta_Pg')
# extract the star_age column of data
ages_1_OC = h_1_OC.data('star_age')
delta_Pi_1_OC = h_1_OC.data('delta_Pg')
# extract the star_age column of data
ages_2_OC = h_2_OC.data('star_age')
delta_Pi_2_OC = h_2_OC.data('delta_Pg')
# extract the star_age column of data
ages_5_OC = h_5_OC.data('star_age')
delta_Pi_5_OC = h_5_OC.data('delta_Pg')

# extract the star_age column of data
center_he4_025_OC = h_025_OC.data('center_he4')
# extract the star_age column of data
center_he4_05_OC = h_05_OC.data('center_he4')
# extract the star_age column of data
center_he4_1_OC = h_1_OC.data('center_he4')
# extract the star_age column of data
center_he4_2_OC = h_2_OC.data('center_he4')
# extract the star_age column of data
center_he4_5_OC = h_5_OC.data('center_he4')

delta_Pi_cond_025_OC = (delta_Pi_025_OC != 0) & (center_he4_025_OC < 0.9)
delta_Pi_cond_05_OC = (delta_Pi_05_OC != 0) & (center_he4_05_OC < 0.9)
delta_Pi_cond_1_OC = (delta_Pi_1_OC != 0) & (center_he4_1_OC < 0.9)
delta_Pi_cond_2_OC = (delta_Pi_2_OC != 0) & (center_he4_2_OC < 0.9)
delta_Pi_cond_5_OC = (delta_Pi_5_OC != 0) & (center_he4_5_OC < 0.9)

fig, axs = plt.subplots(2, 1, figsize=(6, 8))

ax = axs[0]
ax.plot(ages_025_OC[delta_Pi_cond_025_OC], delta_Pi_025_OC[delta_Pi_cond_025_OC], label='0.25_OC')
ax.plot(ages_05_OC[delta_Pi_cond_05_OC], delta_Pi_05_OC[delta_Pi_cond_05_OC], label='0.5_OC')
ax.plot(ages_1_OC[delta_Pi_cond_1_OC], delta_Pi_1_OC[delta_Pi_cond_1_OC], label='1_OC')
ax.plot(ages_2_OC[delta_Pi_cond_2_OC], delta_Pi_2_OC[delta_Pi_cond_2_OC], label='2_OC')
ax.plot(ages_5_OC[delta_Pi_cond_5_OC], delta_Pi_5_OC[delta_Pi_cond_5_OC], label='5_OC')
ax.set_xlabel('age')
ax.set_ylabel('delta_Pg')
plt.legend()

ax = axs[1]
ax.plot(center_he4_025_OC[delta_Pi_cond_025_OC], delta_Pi_025_OC[delta_Pi_cond_025_OC], label='0.25_OC')
ax.plot(center_he4_05_OC[delta_Pi_cond_05_OC], delta_Pi_05_OC[delta_Pi_cond_05_OC], label='0.5_OC')
ax.plot(center_he4_1_OC[delta_Pi_cond_1_OC], delta_Pi_1_OC[delta_Pi_cond_1_OC], label='1_OC')
ax.plot(center_he4_2_OC[delta_Pi_cond_2_OC], delta_Pi_2_OC[delta_Pi_cond_2_OC], label='2_OC')
ax.plot(center_he4_5_OC[delta_Pi_cond_5_OC], delta_Pi_5_OC[delta_Pi_cond_5_OC], label='5_OC')
ax.set_xlabel('center_he4')
plt.gca().invert_xaxis()
plt.ylabel('delta_Pg')
plt.legend()
plt.show()

