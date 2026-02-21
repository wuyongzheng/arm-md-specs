## 14.3 SMMU-originated transactions

An SMMU read for any translation, configuration or queue structure that is performed into any PCIe address space is permitted to return any value or be terminated with an external abort.

Note: Arm expects SMMU structures and translation tables that are accessed externally in non-embedded implementations to be located in system memory. A potential deadlock (where an SMMU read access is dependent on the completion of an incoming PCIe write which is itself dependent on the SMMU translation that caused the original access) can be avoided by the system terminating SMMU accesses targeted to the PCIe domain by malicious or incorrect software.