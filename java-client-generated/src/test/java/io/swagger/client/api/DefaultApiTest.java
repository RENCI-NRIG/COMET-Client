package io.swagger.client.api;

import io.swagger.client.ApiClient;
import io.swagger.client.ApiException;
import io.swagger.client.model.CometResponse;
import io.swagger.client.model.Value;
import org.junit.Test;
import org.junit.Ignore;
import org.json.simple.*;
import java.io.FileInputStream;
import java.io.InputStream;

class CometValue extends Value {
    CometValue(String v) {
        val_ = v;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class Value {\n");
        sb.append(val_);
        sb.append("}");
        return sb.toString();
    }

    private String val_;
}

/**
 * API tests for DefaultApi
 */
@Ignore
public class DefaultApiTest {

    private final ApiClient apiClient= new ApiClient();
    private final DefaultApi api = new DefaultApi(apiClient);
    
    /**
     * Delete scope within a context.  
     *
     * Delete scope within a context.   - Operation requires write access 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteScopeDeleteTest() throws ApiException {
        String contextID = null;
        String family = null;
        String key = null;
        String readToken = null;
        String writeToken = null;
        CometResponse response = api.deleteScopeDelete(contextID, family, key, readToken, writeToken);

        // TODO: test validations
    }
    
    /**
     * Retrieve a list of existing scopes within a given context.   
     *
     * Retrieve a list of existing scopes within a given context.   - Operation requires read access - Returns list of  [ {family, key} ] 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void enumerateScopeGetTest() throws ApiException {
        String contextID = null;
        String readToken = null;
        String family = null;
        CometResponse response = api.enumerateScopeGet(contextID, readToken, family);

        // TODO: test validations
    }
    
    /**
     * Retrieve the current Comet version and Comet API version. 
     *
     * Retrieve the current Comet version and Comet API version. 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getVersionGetTest() throws ApiException {
        CometResponse response = api.getVersionGet();

        // TODO: test validations
    }
    
    /**
     * Retrieve a value from a named scope within a context.  
     *
     * Retrieve a value from a named scope within a context.  - Operation requires read access  Need to distinguish the following situations: - The scope value is null - The scope existed, but was deleted - The scope never existed (for the period of garbage collection) - Scope visibility doesn’t match 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void readScopeGetTest() throws ApiException {
            	try {

	    	apiClient.setBasePath("https://13.58.134.113:8111/");
	    	//InputStream sslCaCert = new FileInputStream("/Users/komalthareja/comet/cometclient.jks");
	    	InputStream sslCaCert = new FileInputStream("/Users/komalthareja/comet/certs.der");
	    	//InputStream sslCaCert = new FileInputStream("/Users/komalthareja/.ssh/geni-kthare10.der");
	    	apiClient.setSslCaCert(sslCaCert);

	        String contextID = "47b7dc35-3557-495a-9d73-40d50c7803db";
	        String family = "interfaces";
	        String key = "6729c69f-d9ff-4223-b52a-b6cda9bfcbef";
	        String readToken = "6729c69f-d9ff-4223-b52a-b6cda9bfcbef-rid";
	        CometResponse response = api.readScopeGet(contextID, family, key, readToken);
	        if (!response.getStatus().equals("OK")) {
	            System.out.println("READSCOPE Status: " + response.getStatus() + "Message: " + response.getMessage());
	            return;
	        }
	        String val = response.getValue().toString();
	        System.out.println("READSCOPE RES: " + val);
	        if(!val.isEmpty()) {
	        	String [] arrOfStr = val.split("=");
	        	if(arrOfStr.length < 2) {
	        		System.out.println("Incorrect response");
	        	}
	        	val = arrOfStr[1].substring(0, arrOfStr[1].length()-1);
	        	System.out.println("DEBUG1 : " + val);
	        	JSONObject o = (JSONObject)JSONValue.parse(val);
	        	System.out.println("DEBUG2 Val is array " + o.get("val_").toString());
	        	JSONArray a = (JSONArray)JSONValue.parse(o.get("val_").toString());
	        	System.out.println("DEBUG3 Val is array " + a.toString());
	        }

    	}
    	catch(ApiException e) {
    		System.out.println("ApiException occured while READSCOPE: " + e.getMessage());
    		e.printStackTrace();
    		throw e;
    	}
    	catch(Exception e) {
    		System.out.println("Exception occured while READSCOPE: " + e.getMessage());
    		e.printStackTrace();
    	}

        // TODO: test validations
    }
    
    /**
     * Create or modify a named scope for slice/sliver within a context, with visibility label (user_key | comet_admin): 
     *
     * Create or modify a named scope for slice/sliver within a context, with visibility label (user_key | comet_admin): - Operation requires write access - Substitute existing value with new value 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void writeScopePostTest() throws ApiException {
    	try {
    		
    	apiClient.setBasePath("https://13.58.134.113:8111/");
    	InputStream sslCaCert = new FileInputStream("/Users/komalthareja/comet/certs.der");
    	apiClient.setSslCaCert(sslCaCert);
        CometValue string = new CometValue("TEST");
        String contextID = "cid";
        String family = "fam";
        String key = "uid";
        String readToken = "uid-rid";
        String writeToken = "uid-wid";
        CometResponse response = api.writeScopePost(string, contextID, family, key, readToken, writeToken);
        System.out.println("Status: " + response.getStatus());
        System.out.println("Message: " + response.getMessage());
    	}
    	catch(ApiException e) {
    		System.out.println("ApiException occured while write: " + e.getMessage());
    		e.printStackTrace();
    		throw e;
    	}
    	catch(Exception e) {
    		System.out.println("Exception occured while write: " + e.getMessage());
    		e.printStackTrace();
    	}        

        // TODO: test validations
    }
    
}
