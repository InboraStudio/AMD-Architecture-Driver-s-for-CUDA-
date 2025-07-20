# CUDA Drivers for AMD Architecture Pipelines Using ROCm

> ⚠️ **Note:** AMD GPUs do **not natively support CUDA**, which is proprietary to NVIDIA.  
> This repository emulates a CUDA-like development environment for AMD GPUs by leveraging AMD’s **ROCm** platform, **HIP (Heterogeneous-compute Interface for Portability)**, and **CI pipelines** to enable **high-performance GPU compute** across **RDNA/CDNA hardware**.

---

## Background

CUDA is **NVIDIA-specific**. It tightly couples hardware and software via proprietary drivers, compilers, and a runtime stack. AMD GPUs **do not** support CUDA natively. But if you're on Team Red (AMD), you’re not left behind—thanks to **HIP** and **ROCm**.


---
## TL;DR for Devs & Engineers  
- **NVIDIA uses:** `CUDA`, `cuDNN`, `nvcc`, `libcudart`, and `PTX kernels`
- **AMD uses:** `HIP`, `ROCm`, `hipcc`, `ROCr runtime`, and `HSACO kernels`
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

## Pros:
- Write once, run on both NVIDIA and AMD
- Familiar to CUDA devs
- Supported by PyTorch, TensorFlow via AMD extensions

---

## Translation Layer: HIP

**HIP (Heterogeneous-Compute Interface for Portability)** is AMD’s CUDA-to-AMD translation layer. It allows CUDA-like syntax with `hipcc` to compile and run on both **AMD** and **NVIDIA**.

```cpp
// HIP example kernel
__global__ void addKernel(float* c, const float* a, const float* b) {
    int i = threadIdx.x;
    c[i] = a[i] + b[i];
}
```
Each ROCm component repo links to this central YAML orchestrator via `rocm-ci.yml`.

---

## Kernel-Level Details

AMD kernel compilation flow:
1. Source (`.hip` or `.cpp`) → LLVM IR
2. LLVM IR → HSA Intermediate Language (HSAIL)
3. HSAIL → **HSACO (HSA Code Object)**
4. Executed on GCN / RDNA via ROCr runtime

_Think of HSACO like NVIDIA’s PTX, but for AMD hardware._

##  Extra: SSSA Form, Vectorization & Tiling

AMD compiler backends (LLVM + HCC) convert kernels into **Static Single Assignment (SSSA)** form for:
-  **Aggressive loop tiling**
-  **SIMD vectorization**
-  **Wavefront-level parallelism** (similar to warps in CUDA)

## Integrations & Support

| Framework        | AMD ROCm / HIP Support |
|------------------|------------------------|
| PyTorch          | ✅ via `ROCm` builds   |
| TensorFlow       | ✅ via `tensorflow-rocm` |
| ONNX Runtime     | ✅                      |
| Blender Cycles   | ✅ (OpenCL backend)     |
| NumPy/SciPy      | ⚠️ Limited (via CuPy HIP port) |

##  Tools for AMD GPU Devs

- `hipcc` – HIP compiler (alias of `clang`)
- `rocminfo` – Device capabilities viewer
- `clinfo` – OpenCL device inspection
- `rocm-smi` – AMD GPU status tool (temp, power, clocks)
- `hipify-perl` – Convert `.cu` files to `.hip`

##  Bonus: Future of AMD AI Stack

- ROCm now supports **AI super-scaling (similar to Tensor Cores)** via `Matrix Cores` in MI300/Instinct series.
- Upcoming **OpenCL 3.0 compliance**
- Potential Vulkan Compute ↔ HIP interop for hybrid render/compute


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
```

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