## Chapter 10 Performance Monitors Extension

## 10.1 Support and discovery

Performance monitoring facilities are optional. When implemented, the SMMU has one or more Performance Monitor Counter Groups (PMCG) associated with it. The discovery and enumeration of a base address for each group is IMPLEMENTATION DEFINED. The Performance Monitor Counter Groups are standalone monitoring facilities and, as such, can be implemented in separate components that are all associated with (but not necessarily part of) an SMMU.

Note: A centralized ID scheme to identify common properties is not currently exploited because PMCGs might be independently-designed, and contain their own identification facilities.