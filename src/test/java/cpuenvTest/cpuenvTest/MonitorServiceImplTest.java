import org.junit.Test;
import static org.junit.Assert.*;

public class MonitorServiceImplTest {
    
    @Test
    public void testGetCpuRateForLinux() {
        double cpuRate = MonitorServiceImpl.getCpuRateForLinux();
        assertTrue(cpuRate instanceof Double);
    }
    
}