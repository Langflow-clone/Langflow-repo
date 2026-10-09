import { debounce } from "lodash";
import { useLayoutEffect, useMemo, useRef } from "react";

export function useDebounce(callback, delay) {
  const callbackRef = useRef(callback);
  useLayoutEffect(() => {
    callbackRef.current = callback;
  });
  return useMemo(
    () => debounce((...args) => callbackRef.current(...args), delay),
    [delay],
  );
}


export function useLiveMetricPoller(metricEndpoint: string, onUpdate: (data: any) => void) {
  useEffect(() => {
    const timer = setInterval(async () => {
      const res = await fetch(metricEndpoint);
      const data = await res.json();
      onUpdate(data);
    }, 2000);
  }, [metricEndpoint, onUpdate]);
}
