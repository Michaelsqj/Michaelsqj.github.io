---
layout: post
title: 问题：
date: 2021-09-25
description: 
tags: 
status: 
---

1. 如何在idea中设置channel
2. 什么是user interface？为什么要用ParameterMap?

# Video tutorial

## 1. IDEA, CVS, makefiles, grep, cygwin, IDEA directory structure, sde commands, compiling, POET, unit test

IDEA版本：VB17运行在xp上是最老的，VD11运行在win7上比较新，VE是最新的运行在linux上，用在PRISMA机器上。VD和VE只是GUI不一样，用的机器不一样，其他都是一样的。但是VB和其他两个差别比较大

unit test

simple unit test: 检查parameters，每次写程序必须是从Siemens提供的程序开始。

extended unit test: 

cygwin: shell on windows

grep: 搜索命令

cvs: version control

## 2. Overview of IDEA sequence programming

<div class="row mt-3"><div class="col-sm mt-3 mt-md-0"><img class="img-fluid rounded z-depth-1" src="{{ site.baseurl }}/assets/img/Siemens%20Sequence%20Programming%2098cd4ee883e442eb8909d55f86530821/Untitled.png" data-zoomable></div></div>

VB17 architecture (different from VE)

由三个不同的电脑，不同系统组成

**MrProt**: data structure 包含了所有的序列信息

**SBB(sequence building block)**: do a specific bit of the pulse sequence (init, prep, run, check function)

**RTEB**(real-time event block) : the actual waveform information

MRIR (MR-image reconstruction computer)

SeqExpo: 告知MRIR一些序列信息，从而执行特定的reconstruction  

**DLLs**:

- compilation:

    compilation of the sequence produce **.dll** rather than executable

    scanner has a **main()** that loads the requested **.dll** at runtime

    compilation also makes ancillary files (**.lib .exp**) with import info for **linking**

- different dll

    on **desktop**, "**debug**" version (e.g., MySequenced.dll)

    on **scanner**, "**release**" version (e.g., MySequence.dll)

    on scanner, there are two .dll, for **host** (**.dll**), for **MPCU** (**.i86**)

**Makefiles**:

two make files (e.g., Mysequence.**mk**, makefile.**trs**)

how to link? **LDLIBS += LibToLink.lib**, **LDDLLS += LibToLink.dll**

**c++ classes**: 

将各种实体硬件等抽象成classes

- Hardware proxy classes: 表示physical amplifier, gradient等
- real-time event classes: 表示pulse sequence component (e.g., RF pulses)
- control classes: 控制程序执行细节 (e.g., looping)
- data classes: 包含proctocol info etc.

**Inheritance**:

从base class不断具体化

e.g., `RTEvent` ⇒ `sGRAD_PULSE_BASE` ⇒ `sGRAD_PULSE_TRAP` ⇒ `sGRAD_PULSE_PE`

### Important data classes

**SeqLim**

proctocol limit (e.g., 50<FOV<500 mm)

set in `fSEQInit`, read-only in `fSEQPrep`

**MrProt**

current sequence proctocol (e.g., FOV=240 mm)

set in `fSEQPrep`

**SeqExpo**

secondary parameters indirectly set by proctocol (e.g., RF energy)

filled in `fSEQPrep` ****, passed to **MRIR**

**Mdh** (measurement data header)

info on **current** data frame (e.g., current PE line is 32)
filled in `fSEQRun`, passed to **MRIR**

### IDEA at 10000 feet (in a broad view), implement fSEQ functions

**fSEQInit**: Run **once** when sequence is selected

- Define “hard limits”, fill in `SeqLim` (absolute max/mins for TR, FOV, etc.)
- Set up **default protocol** (must be a valid protocol!)

**fSEQPrep**: Run on **host** **each time protocol modified**, **once** on **MPCU**

- Use protocol contained in `MrProt` to calculate specific sequence (timings, etc)
- **Binary search mode**: Define “soft limits” (max/mins for parameters given current
protocol... e.g., **max TE given TR**)
- Make sure current **protocol is possible** (protocol must be “consistent”)

**fSEQCheck**: Run **once** on **MCPU** between `fSEQPrep` and `fSEQRun`

- Gradient **safety watchdog**, check “corners” of sequence for stimulation levels

**fSEQRun**: Run **once** on **MCPU** (this is the real action!)

- Implement/oversee real-time sequence events (RTEB, etc)
- Label k-space data with Mdh class (passed to recon computer)

**fSEQRunKernel**: **Optional** function called **within** `fSEQRun` **TR loop**

- Implements **actual real-time events** for current TR

Use **compiler directive** to limit any code section on **host**/ **MPCU**

```cpp
#IFDEF VXWORKS
      // code to be only be executed on MPCU
#ENDIF
#IFNDEF VXWORKS
      // code to be only be executed on host
#ENDIF
```

### IDEA at 5000 feet: Real-time Events

**Real-time events 在 real-time event block中执行**

**Real-Time Events (libRT)**

**Classes** that implement **precisely-timed instructions** for **hardware proxies**
(e.g., Gradient waveforms (`sGRAD_PULSE`), RF pulses (`sRF_PULSE`), ADC readouts (`sREADOUT`), etc.)

**Life cycle of a real-time event**

**Configure**: Set **properties** based on protocol (e.g., **gradient amplitude**)
**Prep**: Calculate specific **details** of event (e.g., **RF waveform**)
**Run**: Place on execution queue (within **real-time event block**)

**Preparation of real-time events**

Prepare pulse with initialized properties

(e.g., gradient pulses: `.prepSymmetricTOTShortestTime()`, `.prepAmplitude()`, `.prepMomentumTOT()`)

Detecting **prep failure** used to detect “**soft limits**” when `fSEQPrep` is run in **binary search mode** (i.e., limits given current parameters)

**Gradients** need to be **validated** against hardware specs with `.check()`

```cpp
// Declare pulse in global section:
static sRF_PULSE_SINC sSRF ("sSRF");

// Set from protocol and prepare in fSEQPrep:
// configure parameters of RF pulse
sSRF.setDuration         (1280) ;
sSRF.setFlipAngle        (pMrProt->flipAngle());
// prep RF pulse
if(! sSRF.prepSinc(pMrProt,pSeqExpo)) return (sSRF.getNLSStatus());

// Insert into event block in fSEQRunKernel: // execute RF pulse in real-time event block
fRTEI( lTRF, 0, &sSRF, 0, 0, 0, 0, 0);

// Alternatively, call run() method in fSEQRunKernel:
// execute RF pulse with “run” statement
sSRF.setStartTime(lTRF);
sSRF.run();
```

### IDEA at 5000 feet: Real-time Event Blocks

**Real-time events 在 real-time event block中执行，分三步**

1. `fRTEBInit` 打开event block
2. `fRTEI` 在指定时间开始所有的events
3. `fRTEBFinish` 关闭event block

<div class="row mt-3"><div class="col-sm mt-3 mt-md-0"><img class="img-fluid rounded z-depth-1" src="{{ site.baseurl }}/assets/img/Siemens%20Sequence%20Programming%2098cd4ee883e442eb8909d55f86530821/Untitled%201.png" data-zoomable></div></div>

**如何设置channel** 

### IDEA at 5000 feet: SBBs and SeqLoop

**Sequence Building Blocks (libSBB)**

- 包含了real-time event block
- SBB可以和low-level real-time event结合

(e.g., SBBCSat (sat pulses), SBBDiffusion (diffusion gradients), SBBEPIReadOut (EPI))

**SeqLoop class**

- `SeqLoop`控制standard looping structure的时间(sequential, interleaved, 3D)
- `fSEQRun` 将控制交给`SeqLoop`, `SeqLoop` 会调用`fSEQRunKernel`

<div class="row mt-3"><div class="col-sm mt-3 mt-md-0"><img class="img-fluid rounded z-depth-1" src="{{ site.baseurl }}/assets/img/Siemens%20Sequence%20Programming%2098cd4ee883e442eb8909d55f86530821/Untitled%202.png" data-zoomable></div></div>

SBB plug-in: 可以自己实现SBB插入到这里，比如spin echo，diffusion

**using ParameterMap library? user interface?**

```cpp
#include      "ParameterMap.h"

//In fSEQInit():
BEGIN_PARAMETER_MAP(pSeqLim, 0, 0);
PARAM("Read Spoiler", "cyc/px", &dReadSpoilCycles, 0.0, 8.0, 0.1, 2.0,
      "UI for readout spoiler gradient");
END_PARAMETER_MAP;

//In fSEQPrep():
PREPARE_PARAMETER_MAP(pMrProt,pSeqLim);
...
UPDATE_PROTOCOL(pMrProt, pSeqLim);
```

## 3. Detailed overview of MiniFLASH example code

**mc**/**ms** ：进行编译，有选项是release / debug

**poet**: 进入simulation环境

```cpp
//must include these two headers
#include "MrServers/MrMeasSrv/SeqIF/sde_allincludes.h"
#include "MrServers/MrImaging/seq/SystemProperties.h"
// NLS_SEV is the dictionary of error code
#define OnErrorReturn(S) if (((S) & NLS_SEV) != NLS_SUCCESS) return(S)
// declare the prototype of fSEQRunKernel, contain the information on single line in k-space
static NLS_STATUS fSEQRunKernel(MrProt*, SeqLin*, SeqExpo*, long, long);
//fSEQInit: initialize the allowed Sequence Limits 0:42:30
NLS_STATUS fSEQInit()
//fSEQPrep: prepare real time elements and calculate energy and timing 0:54:20
//          configure RF puse -> set ADC -> set gradient 
NLS_STATUS fSEQPrep()
//fSEQCheck: check lines at the border of k-space (gradient overflow)
NLS_STATUS fSEQCheck()
//fSEQRun run the sequence 1:51:30
NLS_STATUS fSEQRun()
//fSEQRunKernel 1:56:40
static NLS_STATUS fSEQRunKernel()
```

所有的时间必须是10ms的倍数，因为机器的clock rate是10ms。 

## IDEA VD13D