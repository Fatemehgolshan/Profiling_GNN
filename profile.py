import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.Context().makeRequestRSpec()

# Create a single node in Wisconsin cluster
node = request.RawPC("node1")
node.hardware_type = "c240g5"
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"

# Output the RSpec
portal.context.printRequestRSpec()
