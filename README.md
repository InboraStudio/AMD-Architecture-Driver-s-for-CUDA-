# CUDA Drivers for AMD Architecture Pipelines Using ROCm

> ⚠️ **Note:** AMD GPUs do **not natively support CUDA**, which is proprietary to NVIDIA.  
> This repository emulates a CUDA-like development environment for AMD GPUs by leveraging AMD’s **ROCm** platform, **HIP (Heterogeneous-compute Interface for Portability)**, and **CI pipelines** to enable **high-performance GPU compute** across **RDNA/CDNA hardware**.

---

##  Overview

This project contains **CI/CD orchestration scripts and YAML-based pipelines** used to automate the **build, test, and deployment** of ROCm-compatible GPU compute workloads using **Azure DevOps Pipelines**.

It acts as a bridge between **traditional CUDA-style development** and AMD’s **open compute ecosystem**, supporting:
- Kernel compilation using **LLVM-based HIP-Clang**
- GPU-side task management and dispatch
- Integration with **ROCr runtime**, ROCgdb, and device-level profilers
- AMD GPU-specific system-level acceleration using **SSSA (Shader SIMD Stream Architecture)** and **Wavefront Execution Models**

---

##  Key Concepts & Stack Layers

| Layer              | Description |
|--------------------|-------------|
| **HIP API**        | CUDA-like C++ API for portable kernel code |
| **ROCr Runtime**   | Handles kernel dispatch, memory management, and GPU command queues |
| **ROCm Compiler**  | HIP-Clang frontend; supports SASS-level kernel compilation |
| **HSA (Heterogeneous System Architecture)** | Foundation for communication between CPU and GPU |
| **RDNA/CDNA ISA**  | Instruction set architecture for discrete and data-center AMD GPUs |
| **Azure DevOps Pipelines** | CI system to orchestrate and scale multi-GPU build/test processes |
| **VMSS with Docker** | Enables scalable containerized GPU workloads for HIP build/test |

---

Each ROCm component repo links to this central YAML orchestrator via `rocm-ci.yml`.

---

##  ROCm GPU Compute Support (Advanced)

This project is designed to work with AMD’s modern GPU compute pipeline, including:
- **Kernel Offloading:** HIP kernels are offloaded to dGPU or APU over PCIe/Infinity Fabric via ROCr
- **Wavefront Scheduler:** SIMD32-based warp schedulers for controlling parallelism
- **SSSA Core Tuning:** Runtime toggling of shared memory, VGPR/SGPR registers
- **Multi-GPU Strategy:** ROCm-aware build agents can parallelize workloads across GPU groups
- **LLDB & ROCgdb Debugging:** Attach low-level debuggers in CI to trace kernel failures
- **ROCm Profiler Support:** CI-integrated hooks for collecting kernel execution metrics

---

##  VMSS Setup for HIP Build Agents

Azure VMSS instances provisioned for ROCm builds should include Docker and be ROCm-aware. Use the following `cloud-init` config in the **Custom Data** field during VM creation:

```yaml
#cloud-config

bootcmd:
  - mkdir -p /etc/systemd/system/walinuxagent.service.d
  - echo "[Unit]\nAfter=cloud-final.service" > /etc/systemd/system/walinuxagent.service.d/override.conf
  - sed "s/After=multi-user.target//g" /lib/systemd/system/cloud-final.service > /etc/systemd/system/cloud-final.service
  - systemctl daemon-reload

apt:
  sources:
    docker.list:
      source: deb [arch=amd64] https://download.docker.com/linux/ubuntu $RELEASE stable
      keyid: 9DC858229FC7DD38854AE2D88D81803C0EBFCD88

packages:
  - docker-ce
  - docker-ce-cli
  - libnuma-dev

groups:
  - docker

runcmd:
  - usermod -aG docker $USER
  - systemctl restart docker
  - systemctl enable docker


## Future Enhancements
 - Dynamic Buffer Kernel Dispatch using HIP Streams and Signal Queues

 - Vulkan Interop pipeline for ROCm + Vulkan kernel rendering on RDNA

 - Automatic HIPIFY scanning of CUDA code in Pull Requests

 - SSBO + Async Compute Support for mixed graphics/GPU compute CI tests

 - LLVM Pass Hooks for auto-injecting metrics during device compile

---

## Key References
# ROCm Developer Guide

- HIP Programming Model

- Azure Pipelines YAML Docs

- LLVM for HIP

- AMD GPU ISA

- OpenMP Offloading to AMD

## Disclaimer
This pipeline and its configuration are provided for open experimentation and CI testing of HIP/ROCm workloads. Usage across different GPU architectures (e.g., RDNA2 vs CDNA2) may require manual configuration adjustments.

This repository and its contributors make no guarantees of performance, correctness, or long-term compatibility. ROCm stack is under active development and may break at any time with upstream changes.

# License & Contributors
- AMD ROCm Ecosystem (Thanks)

- Open Source Contributors (Yess)

- ChipSet By: AMD corporation (OG)

- Maintained by: Inbora Studio (Me)