"""
RunPod | API Wrapper | Queries | GPUs
"""

from ..rp_graphql_types import Pod


QUERY_POD = """
query myPods {
    myself {
        pods {
            id
            containerDiskInGb
            costPerHr
            desiredStatus
            dockerArgs
            dockerId
            env
            gpuCount
            imageName
            lastStatusChange
            machineId
            memoryInGb
            name
            podType
            port
            ports
            uptimeSeconds
            vcpuCount
            volumeInGb
            volumeMountPath
            runtime {
                ports{
                    ip
                    isIpPublic
                    privatePort
                    publicPort
                    type
                }
            }
            machine {
                gpuDisplayName
            }
        }
    }
}
"""


def generate_pod_query(pod_id) -> Pod:
    """
    Generate a query for a specific GPU type
    """

    return f"""
    query pod {{
        pod(input: {{podId: "{pod_id}"}}) {{
            id
            containerDiskInGb
            costPerHr
            desiredStatus
            dockerArgs
            dockerId
            env
            gpuCount
            imageName
            lastStatusChange
            machineId
            memoryInGb
            name
            podType
            port
            ports
            uptimeSeconds
            vcpuCount
            volumeInGb
            volumeMountPath
            runtime {{
                ports {{
                    ip
                    isIpPublic
                    privatePort
                    publicPort
                    type
                }}
            }}
            machine {{
                gpuDisplayName
            }}
        }}
    }}
    """
