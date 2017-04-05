Name:           nvenc
Version:        7.1.9
Release:        4%{?dist}
Summary:        A comprehensive set of APIs for hardware accelerated video encode and decode

License:        https://developer.nvidia.com/nvidia-video-codec-sdk-license-agreement, Redistributable, no modification permitted
URL:            https://developer.nvidia.com/nvidia-video-codec-sdk
Source0:        https://github.com/UnitedRPMs/nvenc/releases/download/%{version}/Video_Codec_SDK_%{version}.zip

BuildArch:      noarch

Provides:       nvidia-video-codec-sdk = %{version}-%{release}
Obsoletes:      nvidia-video-codec-sdk < %{version}-%{release}
Provides:       nvenc-devel = %{version}-%{release}
Obsoletes:      nvenc-devel < %{version}-%{release}

%description
NVIDIA Products with the Kepler, Maxwell and Pascal generation GPUs contain a
dedicated accelerator for video encoding, called NVENC and a dedicated
accelerator for video decoding, called NVDEC, on the GPU die.

While using the dedicated hardware for encode or decode, the GPU’s CUDA cores
and system CPU are free to run other compute-intensive tasks.

NVENCODE API enables software developers to configure this dedicated hardware
video encoder. This dedicated accelerator encodes video at higher speeds and
power efficiency than CUDA-based or CPU-based encoders at equivalent quality.
NVENCODE API allows the programmer to control various settings of the encoder
to set the desired tradeoff between quality and performance.

NVDECODE API enables software developers to configure this dedicated hardware
video decoder. This dedicated accelerator supports hardware-accelerated decoding
of the following video codecs on Windows and Linux platforms: MPEG-2, VC-1,
H.264 (AVCHD), H.265 (HEVC), VP8, VP9.

Note: For Video Codec SDK 7.0, NVCUVID has been renamed to NVDECODE API.

%package samples
Summary:        nvEncoder Sample application source code
Requires:       %{name} = %{version}-%{release}

%description samples
This package contains nvEncoder Sample application source code demonstrating
various encoding capabilities.

%prep
%setup -q -n Video_Codec_SDK_%{version}

%install
install -m 644 -p -D Samples/common/inc/nvEncodeAPI.h \
    %{buildroot}%{_includedir}/%{name}/nvEncodeAPI.h
ln -sf %{_includedir}/%{name}/nvEncodeAPI.h Samples/common/inc/nvEncodeAPI.h

%files
%license LicenseAgreement.pdf
%doc doc/*.pdf Release_notes.txt ReadMe.txt
%{_includedir}/%{name}

%files samples
%license LicenseAgreement.pdf
%doc Samples

%changelog

* Wed Apr 05 2017 David Vásquez <davidva AT tutanota DOT com> - 7.1.9-4
- Upstream

* Sun Jan 08 2017 Simone Caronni <negativo17@gmail.com> - 7.1.9-1
- Update to 7.1.9.

* Fri Aug 19 2016 Simone Caronni <negativo17@gmail.com> - 7.0.1-1
- Update to 7.0.1.
- Runtime requires drivers 367.35+ and adds support for Pascal GPUs.

* Wed Jan 06 2016 Simone Caronni <negativo17@gmail.com> - 6.0.1-1
- Update to 6.0.1.

* Fri Apr 10 2015 Simone Caronni <negativo17@gmail.com> - 5.0.1-1
- First build.
