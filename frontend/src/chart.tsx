"use client"

import { useEffect, useState, useMemo } from "react"
import {
  CartesianGrid,
  Line,
  LineChart,
  XAxis,
  Tooltip as RechartsTooltip,
  ResponsiveContainer,
} from "recharts"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

type ChartProps = {
  selectedChart: string
}


const chartColor = "#6366f1" 

export function Chart({ selectedChart }: ChartProps) {
  const [chartData, setChartData] = useState<any[]>([])

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch(`http://localhost:8000/api/chart-data/${selectedChart}`)
        if (!res.ok) throw new Error("Network error")
        const data = await res.json()
        setChartData(data)
      } catch (err) {
        console.error("Failed to fetch data:", err)
      }
    }

    if (selectedChart !== "none") {
      fetchData()
    }
  }, [selectedChart])

  
  const dataKey = useMemo(() => {
    if (chartData.length > 0) {
      const keys = Object.keys(chartData[0])
      return keys.find(k => k !== "date") || "value"
    }
    return "value"
  }, [chartData])

  return (
    <>

      <Card className="py-4 sm:py-0">
        <CardHeader className="flex flex-col items-stretch border-b !p-0 sm:flex-row">
          <div className="flex flex-1 flex-col justify-center gap-1 px-6 pb-3 sm:pb-0">
            <CardTitle>{selectedChart} Chart</CardTitle>
            <CardDescription>Analytics data plotted over time</CardDescription>
          </div>
        </CardHeader>

        <CardContent className="px-2 sm:p-6">
          {chartData.length > 0 ? (
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={chartData} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  dataKey="date"
                  tickLine={false}
                  axisLine={false}
                  tickFormatter={(value) => {
                    const date = new Date(value)
                    return date.toLocaleDateString("en-US", {
                      month: "short",
                      day: "numeric",
                    })
                  }}
                  minTickGap={32}
                />
                <RechartsTooltip
                  formatter={(value: number) => value.toFixed(4)}
                  labelFormatter={(value) =>
                    new Date(value).toLocaleDateString("en-US", {
                      month: "short",
                      day: "numeric",
                      year: "numeric",
                    })
                  }
                />
                <Line
                  type="monotone"
                  dataKey={dataKey}
                  stroke={chartColor}
                  strokeWidth={2}
                  dot={false}
                />
              </LineChart>
            </ResponsiveContainer>
          ) : (
            <div className="text-center text-gray-400">No data available</div>
          )}
        </CardContent>
      </Card>
    </>
  )
}