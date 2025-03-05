import geni.portal as portal
import geni.rspec.pg as rspec

# Define parameters
portal.context.defineParameter("node_type", "Select Node Type", portal.ParameterType.STRING, "d7525")

# Create Request
request = portal.Context().makeRequestRSpec()

# Create a node
node = request.RawPC("node1")
node.hardware_type = portal.context.bindParameter("node_type")
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"

# Output RSpec
portal.context.printRequestRSpec()
