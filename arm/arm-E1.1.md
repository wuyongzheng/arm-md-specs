## E1.1 About the Application level programmers' model

This chapter contains the programmers' model information required for the development of applications that execute in AArch32 state.

The information in this chapter is distinct from the system information required to service and support application execution under an operating system, or higher level of system software. However, some knowledge of that system information is needed to put the Application level programmers' model into context.

Depending on the implementation, the architecture supports multiple levels of execution privilege. These privilege levels are indicated by different Exception levels that number upwards from EL0, where EL0 corresponds to the lowest privilege level and is often described as unprivileged . The Application level programmers' model is the programmers' model for software executing at EL0. For more information, see Arm architectural concepts.

System software determines the Exception level, and therefore the level of privilege, at which application software runs. When an operating system supports execution at both EL1 and EL0, an application usually runs unprivileged. This has the following effects:

- It means that the operating system can allocate system resources to an application in a unique or shared manner.
- It provides a degree of protection from other processes, and so helps protect the operating system from malfunctioning software.

This chapter indicates where some System level understanding is helpful, and if appropriate it gives a reference to the System level description.

Application level software is generally unaware of its Security state, and of any virtualization. For more information, see The Armv8-A security model and The effect of implementing EL2 on the Exception model.

Note

- When an implementation includes EL3, application and operating system software normally executes in Nonsecure state.
- Older documentation, describing implementations or architecture versions that support only two privilege levels, often refers to execution at EL1 as privileged execution.