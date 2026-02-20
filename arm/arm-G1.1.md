## G1.1 About the AArch32 System level programmers' model

An application programmer has only a restricted view of the system. The System level programmers' model supports this application level view of the system, and includes features that are required for one or both of an operating system (OS) and a hypervisor to provide the programming environment seen by an application. This chapter describes the System level programmers' model when executing at EL1 or higher in an Exception level that is using AArch32.

The system level programmers' model includes all of the system features required to support operating systems and to handle hardware events.

The following sections give a system level introduction to the basic concepts of the Arm architecture AArch32 state, and the terminology that is used for describing the architecture when executing in this state:

- Exception levels.
- Exception terminology.
- Execution state.
- Instruction Set state.
- Security state.
- Virtualization.

The rest of this chapter describes the system level programmers' model when executing in AArch32 state.

The other chapters in this part describe:

- The memory system architecture, as seen when executing in an Exception level that is using AArch32:
- -The AArch32 System Level Memory Model describes the general features of the Armv8 memory model, when executing in AArch32 state, that are not visible at the application level.

Note

The AArch32 Application Level Memory Model describes the application level view of the memory model.

- -The AArch32 Virtual Memory System Architecture describes the Virtual Memory System Architecture (VMSA) used in AArch32 state.
- The AArch32 System registers, see AArch32 System Register Descriptions.

Note

The T32 and A32 instruction sets include instructions that provide system level functionality, such as returning from an exception. See, for example, ERET.