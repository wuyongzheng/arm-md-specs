## 12.3 Service Failure Mode (SFM)

If internal consistency is known to have been lost (for example, detection of a UE in internal register state), or there is a likelihood that it has been lost, and the functionality of the SMMU will be impaired or would risk silent data corruption or silent propagation of errors, Service Failure Mode must be entered. The SMMU must terminate client transactions after this mode is entered, and stop accessing its queues. If an SMMU is in Service Failure Mode (SFM) it responds to PCIe requests as CA wherever possible. Arm recommends that the SMMU registers are still readable in this mode to aid diagnosis. The mechanism to exit or recover from this mode is IMPLEMENTATION DEFINED, but must include system reset.

Note: An implementation might have specific isolation features or safety guarantees. For example, a partitioning system in which some client devices are guaranteed to be unaffected by a loss of consistency in a different portion of the SMMU. When a Detected Uncorrected Error occurs in an isolated manner like this, the SMMU does not enter the general Service Failure Mode, and does not raise the SMMU\_(S\_)GERROR.SFM\_ERR error.

Entry to Service Failure Mode is signaled by all of the following means:

- The Global Errors SMMU\_GERROR.SFM\_ERR and SMMU\_S\_GERROR.SFM\_ERR are triggered for both Non-secure and Secure programming interfaces (if implemented).
- An IMPLEMENTATION DEFINED notification such as recording syndrome into RAS registers and asserting an Error Recovery Interrupt or system-wide error interrupt.

Diagnosis of the reason for entering SFM is made through IMPLEMENTATION DEFINED means.