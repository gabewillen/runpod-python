"""
RunPod | API Wrapper | GraphQL Types

These types were automatically generated using runpod_typegen and https://graphql-spec.runpod.io/.

"""

from typing import TypedDict, Optional, List
from enum import StrEnum
from datetime import date, datetime


class ApiKey(TypedDict):
    id: Optional[str]


class AuditLog(TypedDict):
    actorId: Optional[str]


class AuditLogConnection(TypedDict):
    edges: Optional[List["AuditLog"]]


class BenchmarkPod(TypedDict):
    id: Optional[str]


class BillingGranularity(StrEnum):
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class ClientCreditCharge(TypedDict):
    amount: Optional[float]


class ClientCreditChargeType(StrEnum):
    CHARGE_SERVERLESS = "CHARGE_SERVERLESS"
    CHARGE_POD = "CHARGE_POD"
    CHARGE_API = "CHARGE_API"
    CHARGE_STORAGE = "CHARGE_STORAGE"
    CHARGE_SAVINGS_PLAN = "CHARGE_SAVINGS_PLAN"


class CloudTypeEnum(StrEnum):
    SECURE = "SECURE"
    COMMUNITY = "COMMUNITY"
    ALL = "ALL"


class Compliance(StrEnum):
    GDPR = "GDPR"
    ISO_IEC_27001 = "ISO_IEC_27001"
    ISO_14001 = "ISO_14001"
    PCI_DSS = "PCI_DSS"
    HITRUST = "HITRUST"
    SOC_1_TYPE_2 = "SOC_1_TYPE_2"
    SOC_2_TYPE_2 = "SOC_2_TYPE_2"
    SOC_3_TYPE_2 = "SOC_3_TYPE_2"
    ITAR = "ITAR"
    FISMA_HIGH = "FISMA_HIGH"


class ComputeType(StrEnum):
    CPU = "CPU"
    GPU = "GPU"


class ContainerRegistryAuth(TypedDict):
    id: Optional[str]


class CpuFlavor(TypedDict):
    id: Optional[str]


class CpuType(TypedDict):
    id: Optional[str]


class CreditCode(TypedDict):
    id: Optional[str]


class CsrRole(StrEnum):
    admin = "admin"
    support_write = "support_write"
    support_read = "support_read"


class DataCenter(TypedDict):
    id: Optional[str]


class DataCenterStorage(TypedDict):
    hostname: Optional[str]


class DataCenterStorageList(TypedDict):
    mnt: Optional[str]


class Discount(TypedDict):
    userId: str


class DiscountType(StrEnum):
    SERVERLESS = "SERVERLESS"


class EarningsCustomRangeInput(TypedDict):
    startDate: date


class Endpoint(TypedDict):
    aiKey: Optional[str]


class EndpointStatisticGranularity(StrEnum):
    LIVE = "LIVE"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class EnvironmentVariable(TypedDict):
    key: Optional[str]


class EnvironmentVariableInput(TypedDict):
    key: str


class Gpu(TypedDict):
    id: str


class GpuAvailability(TypedDict):
    available: Optional[bool]


class GpuAvailabilityInput(TypedDict):
    gpuCount: Optional[int]


class GpuLowestPriceInput(TypedDict):
    countryCode: Optional[str]


class GpuTelemetry(TypedDict):
    id: Optional[str]


class GpuType(TypedDict):
    lowestPrice: Optional["LowestPrice"]


class GpuTypeFilter(TypedDict):
    id: Optional[str]


class Impersonation(TypedDict):
    auditLogs: Optional["AuditLogConnection"]


class LowestPrice(TypedDict):
    gpuName: Optional[str]


class Machine(TypedDict):
    pods: Optional[List["Pod"]]


class MachineBalance(TypedDict):
    hostDiskEarnings: Optional[float]


class MachineBenchmark(TypedDict):
    errors: Optional[str]


class MachineEarning(TypedDict):
    name: Optional[str]


class MachineMaintenance(TypedDict):
    id: Optional[str]


class MachineSummary(TypedDict):
    cpuTypeId: Optional[str]


class MachineSystem(TypedDict):
    os: Optional[str]


class MachineTelemetry(TypedDict):
    time: Optional[datetime]


class MachineUptime(TypedDict):
    error: Optional[str]


class NetworkStorageEarning(TypedDict):
    date: Optional[datetime]


class NetworkStorageEarningInput(TypedDict):
    granularity: Optional[str]


class NetworkVolume(TypedDict):
    id: Optional[str]


class PageInfo(TypedDict):
    endCursor: Optional[datetime]


class Pod(TypedDict):
    lowestBidPriceToResume: Optional[float]


class PodBidResumeInput(TypedDict):
    podId: str


class PodEditJobInput(TypedDict):
    podId: str


class PodFilter(TypedDict):
    podId: str


class PodFindAndDeployOnDemandInput(TypedDict):
    aiApiId: Optional[str]


class PodMachineInfo(TypedDict):
    id: Optional[str]


class PodRegistry(TypedDict):
    auth: Optional[str]


class PodRentInterruptableInput(TypedDict):
    bidPerGpu: Optional[float]


class PodResumeInput(TypedDict):
    podId: str


class PodRuntime(TypedDict):
    container: Optional["PodRuntimeContainer"]


class PodRuntimeContainer(TypedDict):
    cpuPercent: Optional[int]


class PodRuntimeGpus(TypedDict):
    id: Optional[str]


class PodRuntimePorts(TypedDict):
    ip: Optional[str]


class PodStatus(StrEnum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    RESTARTING = "RESTARTING"
    EXITED = "EXITED"
    PAUSED = "PAUSED"
    DEAD = "DEAD"
    TERMINATED = "TERMINATED"


class PodStopInput(TypedDict):
    podId: str


class PodTelemetry(TypedDict):
    state: Optional[str]


class PodTemplate(TypedDict):
    advancedStart: Optional[bool]


class PodTerminateInput(TypedDict):
    podId: str


class PodType(StrEnum):
    INTERRUPTABLE = "INTERRUPTABLE"
    RESERVED = "RESERVED"
    BID = "BID"
    BACKGROUND = "BACKGROUND"


class SaveRegistryAuthInput(TypedDict):
    name: str


class SavingsPlan(TypedDict):
    endTime: Optional[datetime]


class SavingsPlanInput(TypedDict):
    planLength: Optional[str]


class Scope(StrEnum):
    CSR_ADMIN = "CSR_ADMIN"
    CSR_IMPERSONATION = "CSR_IMPERSONATION"
    CSR_READ = "CSR_READ"
    CSR_WRITE = "CSR_WRITE"
    TEAM_ADMIN = "TEAM_ADMIN"
    TEAM_DEV = "TEAM_DEV"
    TEAM_BILLING = "TEAM_BILLING"
    TEAM_BASIC = "TEAM_BASIC"
    HOST = "HOST"


class Secret(TypedDict):
    id: str


class Specifics(TypedDict):
    stockStatus: Optional[str]


class SpecificsInput(TypedDict):
    instanceId: Optional[str]


class SpendDetails(TypedDict):
    localStoragePerHour: Optional[float]


class StripeReloadTransaction(TypedDict):
    id: Optional[str]


class Team(TypedDict):
    id: Optional[str]


class TeamInvite(TypedDict):
    id: str


class TeamInviteOwner(TypedDict):
    email: Optional[str]


class TeamInviteTeam(TypedDict):
    id: str


class TeamMembership(TypedDict):
    id: str


class TeamRole(StrEnum):
    owner = "owner"
    admin = "admin"
    member = "member"
    dev = "dev"
    billing = "billing"
    basic = "basic"


class TeamScopes(TypedDict):
    role: Optional[str]


class TransactionMedium(StrEnum):
    STRIPE = "STRIPE"
    CRYPTO = "CRYPTO"
    RUNPOD = "RUNPOD"
    COINBASE = "COINBASE"
    WIRE = "WIRE"
    REFERRAL = "REFERRAL"


class TransactionType(StrEnum):
    RELOAD = "RELOAD"
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    PAYOUT = "PAYOUT"


class User(TypedDict):
    pods: Optional[List["Pod"]]


class UserBilling(TypedDict):
    gpuCloud: Optional[List["UserGpuCloudBilling"]]


class UserBillingInput(TypedDict):
    granularity: Optional["BillingGranularity"]


class UserCpuCloudBilling(TypedDict):
    cpuFlavorId: Optional[str]


class UserGpuCloudBilling(TypedDict):
    gpuTypeId: Optional[str]


class UserInformation(TypedDict):
    firstName: Optional[str]


class UserMachinesFilter(TypedDict):
    start: Optional[int]


class UserReferral(TypedDict):
    code: str


class UserReferralMonth(TypedDict):
    totalReferrals: Optional[int]


class UserRunpodEndpointBilling(TypedDict):
    time: Optional[datetime]


class UserServerlessBilling(TypedDict):
    time: Optional[datetime]


class UserServerlessBillingGroupBy(StrEnum):
    GPU_TYPE = "GPU_TYPE"
    ENDPOINT = "ENDPOINT"
    INSTANCE_ID = "INSTANCE_ID"


class UserServerlessBillingInput(TypedDict):
    groupBy: Optional["UserServerlessBillingGroupBy"]


class UserStorageBilling(TypedDict):
    time: Optional[datetime]


class UserSummaryBilling(TypedDict):
    time: Optional[datetime]


class WebhookRequestStatus(TypedDict):
    time: Optional[datetime]


class WebhookRequestsInput(TypedDict):
    granularity: Optional["EndpointStatisticGranularity"]


class WorkerState(TypedDict):
    time: Optional[datetime]


class WorkerStateInput(TypedDict):
    granularity: Optional["EndpointStatisticGranularity"]


class backgroundPodTelemetryInput(TypedDict):
    machineId: Optional[str]
