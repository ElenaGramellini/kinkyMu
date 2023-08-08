
#File with a header and event list.
#The header listis the simulation conditions:
# - x,y,z, phi, theta energy distributions
# - detector size and location

#Event list has 4 columns:
#- Event ID, Energy, Lenght, theta


from utilities import EventWriter

# Create an instance of the EventWriter class and specify the filename
event_writer = EventWriter('events.csv')

# Define the header for the CSV file
header = ['Event_ID', 'Energy', 'Lenght', 'Theta']

# Write the header to the CSV file
event_writer.headerWriter(header)

# Example event data
event1 = [1]
event2 = [2]
event3 = [3]

# Write each event to the CSV file
event_writer.writeEvent(event1)
event_writer.writeEvent(event2)
event_writer.writeEvent(event3)

