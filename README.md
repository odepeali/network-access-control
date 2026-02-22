I built a simple Network Access Control (NAC) simulation in Python to demonstrate how enterprise access enforcement works at the point of network entry.
This script models three core NAC control layers:
* Authentication Layer: Validates user identity against an authorized credential store.
* Posture Assessment Layer: Verifies device compliance (e.g., OS patch status).
* Policy Enforcement Layer: Dynamically determines access level based on validation results.
  
To demonstrate real world NAC behavior, I ran three separate instances of the simulation:
• Instance 1: Invalid credentials = Access Denied.
• Instance 2: Valid user, non-compliant device = Restricted Access.
• Instance 3: Valid user + compliant device = Full Network Access Granted.
This mirrors how enterprise NAC solutions operate using 802.1X authentication, Radius validation, and dynamic segmentation policies.
