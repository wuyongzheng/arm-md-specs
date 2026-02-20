## G4.1 About the memory system architecture

The Arm architecture supports different implementation choices for the memory system microarchitecture and memory hierarchy, depending on the requirements of the system being implemented. In this respect, the memory system architecture describes a design space in which an implementation is made. The architecture does not prescribe a particular form for the memory systems. Key concepts are abstracted in a way that permits implementation choices to be made while enabling the development of common software routines that do not have to be specific to a particular microarchitectural form of the memory system. For more information about the concept of a hierarchical memory system, see Memory hierarchy.

## G4.1.1 Form of the memory system architecture

The A-profile architecture includes a Virtual Memory System Architecture (VMSA). The AArch32 Virtual Memory System Architecture describes the AArch32 view of the VMSA.

## G4.1.2 Memory attributes

Memory types and attributes describes the memory attributes, including how different memory types have different attributes. Each location in memory has a set of memory attributes, and the translation tables define the virtual memory locations, and the attributes for each location.

Table G4-1 shows the memory attributes that are visible at the system level.

Table G4-1 Memory attribute summary

| Memory type   | Shareability       | Cacheability                                |
|---------------|--------------------|---------------------------------------------|
| Device a      | Outer Shareable.   | Non-cacheable.                              |
| Normal        | One of:            | One of b :                                  |
|               | • Non-shareable.   | • Non-cacheable. • Write-Through Cacheable. |
|               | • Inner Shareable. |                                             |
|               | • Outer Shareable. | • Write-Back Cacheable.                     |

For more information on Cacheability and Shareability, see The Cacheability and Shareability memory attributes, Non-shareable Normal memory, and Caches and memory hierarchy.