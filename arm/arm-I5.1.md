## I5.1 About the external system control register descriptions

This chapter describes the external system control registers other than the external debug registers. That is, it describes:

## An external view of the Performance Monitors registers

Arm recommends that implementations provide access to the Performance Monitors registers through the OPTIONAL External debug interface, and provide the OPTIONAL memory-mapped interface to this interface:

- External Performance Monitors registers summary lists the registers that are accessible in this view of the Performance Monitors, and describes their memory map.
- Performance Monitors external register descriptions describes each of the memory-mapped registers.

Recommended External Interface to the Performance Monitors describes the recommended interface to these registers.

## Note

The Performance Monitors Extension describes the Performance Monitors. The following sections describe the System register interfaces to the Performance Monitors:

- Performance Monitors registers, for accesses from an Exception level that is using AArch64.
- Performance Monitors registers, for accesses from an Exception level that is using AArch32.

## An external view of the Activity Monitors Extension registers

An implementation which supports the Activity Monitors Extension may support an optional external memory-mapped interface to the Activity Monitors Extension registers.

- External Activity Monitors Extension registers summary lists the registers that are accessible in this view of the Performance Monitors, and describes their memory map.
- Activity Monitors external register descriptions describes each of the memory-mapped registers.

Recommended External Interface to the Activity Monitors describes the recommended interface to these registers.

Note

The Activity Monitors Extension describes the Activity Monitors. The following sections describe the System register interfaces to the Activity Monitors:

- Activity Monitors registers, for accesses from an Exception level that is using AArch64.
- Activity Monitors registers, for accesses from an Exception level that is using AArch32.

## The registers for the system level Generic Timer component

Any implementation that includes the Generic Timer must include the memory-mapped system level component described in System Level Implementation of the Generic Timer. In this chapter:

- Generic Timer memory-mapped registers overview gives an overview of the registers, referring to System Level Implementation of the Generic Timer for more information.
- Generic Timer memory-mapped register descriptions describes each of the memory-mapped registers.

Note

The Generic Timer in AArch64 state describes the Generic Timer component that is accessible using the System registers. The following sections describe the System register interfaces to that component:

- Generic Timer registers, for accesses from an Exception level that is using AArch64.
- Generic Timer registers, for accesses from an Exception level that is using AArch32.

Note

External Debug Register Descriptions describes the external debug registers.

Arm ® Memory System Resource Partitioning and Monitoring (MPAM) System Component Specification* (ARM IHI 0099)* describes the MPAM memory-mapped registers.

Arm ® Reliability, Availability, and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100) describes the RAS memory-mapped registers.