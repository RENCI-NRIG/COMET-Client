package org.renci.io.swagger.client.api;

import org.junit.Test;
import org.renci.io.swagger.client.ApiClient;
import org.renci.io.swagger.client.ApiException;
import org.renci.io.swagger.client.api.DefaultApi;
import org.renci.io.swagger.client.model.CometResponse;
import org.renci.io.swagger.client.model.Value;
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
            InputStream sslCaCert = new FileInputStream("/Users/komalthareja/comet/inno-hn_exogeni_net/DigiCertCA.der");
            apiClient.setSslCaCert(sslCaCert);
            KeyStore ks = KeyStore.getInstance("JKS");
            InputStream sslClientCert = new FileInputStream("/Users/komalthareja/comet/inno-hn_exogeni_net/client.jks");
            String ksPwd = "changeme";
            ks.load(sslClientCert, ksPwd.toCharArray());
            KeyManagerFactory keyManagerFactory = KeyManagerFactory.getInstance("SunX509");
            keyManagerFactory.init(ks, ksPwd.toCharArray());
            apiClient.setKeyManagers(keyManagerFactory.getKeyManagers());
            apiClient.applySslSettings();

            String contextID = "39876c7b-f31b-43f3-b4d2-3ff0fb948cbd";
            String family = "interfaces";
            String key = "b55acc64-b376-4a9a-bc3f-70bdae153982";
            String readToken = "80136948-f599-4f31-9d77-50864e02d7dc";
            CometResponse response = api.readScopeGet(contextID, family, key, readToken);
            if (!response.getStatus().equals("OK")) {
                System.out.println("READSCOPE Status: " + response.getStatus() + "Message: " + response.getMessage());
                return;
            }
            String val = response.getValue().toString();
            System.out.println("READSCOPE RES: " + val);

            com.google.gson.internal.LinkedTreeMap o1 = (com.google.gson.internal.LinkedTreeMap) response.getValue();
            if( o1 != null) {
                if(o1.containsKey("value")) {
                    System.out.println("NEucaCometInterface::read: value=" + o1.get("value"));
                    JSONObject o2 = (JSONObject)JSONValue.parse(o1.get("value").toString());
                    if(o2 != null) {
                        if(o2.containsKey("val_")) {
                            System.out.println("NEucaCometInterface::read: val_=" + o2.get("val_"));
                            JSONArray a = (JSONArray)JSONValue.parse(o2.get("val_").toString());
                            System.out.println("Result: " + a.toString() + " size: " + a.size());
                        }
                        else {
                            System.out.println("NEucaCometInterface::read: Unable to get JSONArray val_");
                        }
                    }
                    else {
                        System.out.println("NEucaCometInterface::read: Unable to get JSONObject value");
                    }
                }
                else {
                    System.out.println("NEucaCometInterface::read: CometResponse does not contain value");
                }
            }
            else {
                System.out.println("NEucaCometInterface::read: unable to load json object from CometResponse");
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
