import geni.portal as portal
import geni.rspec.pg as rspec

# Define parameters
pc = portal.Context()
pc.defineParameter("node_type", "Select Node Type", portal.ParameterType.STRING, "d7525")

# Bind parameters
params = pc.bindParameters()

# Create Request
request = pc.makeRequestRSpec()

# Create a node
node = request.RawPC("node1")
node.hardware_type = params.node_type
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"

# Print the request RSpec
pc.printRequestRSpec()
