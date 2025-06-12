#  Large File Generator in Python

This Python script helps you generate large binary files (e.g., multiple GBs) using `os.urandom`. It's a handy tool for testing disk performance, network transfer speeds, backup systems, and more.

---

## 🎯 Features

- Generate files of arbitrary size (in GB).
- Useful for performance testing and simulation.
- Simple and memory-efficient design.
- Optionally add progress bar or automatic file deletion.

---

## 💡 Why This Tool?

Generating large files manually can be time-consuming or inefficient. This script automates that and supports the following real-world **use cases**:

---

### ✅ 1. Disk I/O Benchmarking
- **Use:** Measure how fast your disk can write data.
- **Example:** Compare SSD vs HDD write speeds.
- **Real world:** Data centers, system admins testing new hardware.

---

### ✅ 2. Network Testing (with generated files)
- **Use:** Test how fast a network can transfer large files.
- **Example:** FTP, HTTP, or SFTP file upload/download test.
- **Real world:** Network engineers, DevOps engineers.

---

### ✅ 3. Backup & Restore System Testing
- **Use:** Validate how long it takes to back up or restore large files.
- **Example:** Creating dummy backup archives.
- **Real world:** IT backup systems, cloud storage services.

---

### ✅ 4. Stress Testing Applications
- **Use:** See if an application can handle large file input/output.
- **Example:** Media processing apps, file editors, data migration tools.
- **Real world:** Software QA testers.

---

### ✅ 5. Space Consumption Simulation
- **Use:** Fill disk to see how system behaves under low-disk space.
- **Example:** Simulate low-storage warnings or behavior.
- **Real world:** Embedded system devs, OS developers.

---

### ✅ 6. Forensics and Recovery Tools Testing
- **Use:** See if recovery tools can identify patterns or handle large binary blobs.
- **Example:** Deleted large files recovery.
- **Real world:** Cybersecurity or digital forensics experts.

---

### ✅ 7. Cloud Storage Cost Estimation
- **Use:** Upload large files to check pricing tiers and behavior.
- **Example:** Upload to AWS S3, Google Cloud Storage, etc.
- **Real world:** Cloud architects, IT procurement teams.

---

## 🚀 How to Use

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/large-file-generator.git
cd large-file-generator
