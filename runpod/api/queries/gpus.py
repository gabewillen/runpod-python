"""
RunPod | API | Queries | GPUs
"""

import typing
from ..rp_graphql_types import GpuType


QUERY_GPU_TYPES = """
query GpuTypes {
  gpuTypes {
    id
    displayName
    memoryInGb
  }
}
"""


def generate_gpu_query(gpu_id, gpu_count=1) -> typing.List[GpuType]:
    """
    Generate a query for a specific GPU type
    """

    return f"""
    query GpuTypes {{
      gpuTypes(input: {{id: "{gpu_id}"}}) {{
        maxGpuCount
        id
        displayName
        manufacturer
        memoryInGb
        cudaCores
        secureCloud
        communityCloud
        securePrice
        communityPrice
        oneMonthPrice
        threeMonthPrice
        oneWeekPrice
        communitySpotPrice
        secureSpotPrice
        lowestPrice(input: {{gpuCount: {gpu_count}}}) {{
          minimumBidPrice
          uninterruptablePrice
        }}
      }}
    }}
    """
