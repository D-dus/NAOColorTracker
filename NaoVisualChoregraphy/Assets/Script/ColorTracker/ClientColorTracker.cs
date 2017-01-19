using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Threading;

public class ClientColorTracker : MonoBehaviour {
	
	
	private string mIpAddress;
	private int mPortNumber;
	private Socket mClientSocket;
	private IPAddress mIP;
	private IPEndPoint mIPEP;
	private byte[] mBuffer;
	private byte[] mBufferThread;
	private bool mIsConnectionStarted;
	private byte[] mReceivedBuffer;
	private bool mIsEndOfFrame;
	private Thread ReceivedThread;
	[SerializeField]
	private Text mConsoleText;
	[SerializeField]
	private GameObject mScreenShot;
	private AutoResetEvent mResetEvent;

	// Use this for initialization
	void Start () 
	{
		mIpAddress = "127.0.0.1";
		mPortNumber = 4321;
		mClientSocket = new Socket (AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
		mIP = IPAddress.Parse (mIpAddress);
		mIPEP = new IPEndPoint (mIP, mPortNumber);
		mBuffer = mScreenShot.GetComponent<ScreenShot>().GetBufferToSend();
		mResetEvent = new AutoResetEvent (false);
		
	}
	void Update()
	{
		mBuffer = mScreenShot.GetComponent<ScreenShot> ().GetBufferToSend();
		if(mReceivedBuffer!=null)
		{
			string lTemp=Encoding.ASCII.GetString(mReceivedBuffer);
			mConsoleText.text=lTemp;

		}
	}
	void FixedUpdate()
	{
		mResetEvent.Set ();
	}
	public void StartConnection()
	{
		ReceivedThread = new Thread (TestThread);
		ReceivedThread.Start ();
	}
	public void CloseConnection()
	{
		ReceivedThread.Abort ();
		mClientSocket.Disconnect (true);
	}
	
	private void TestThread()
	{
		while(true)
		{
			mResetEvent.WaitOne();
			if(!mClientSocket.IsBound)
				mClientSocket.Connect(mIPEP);
			else
			{
				mClientSocket.Send (mBuffer, mBuffer.Length, SocketFlags.None);
				if(mReceivedBuffer==null)
					mReceivedBuffer=new byte[mClientSocket.ReceiveBufferSize];
				else
					mClientSocket.Receive(mReceivedBuffer);
			}
		}
	}
	
	void OnApplicationQuit()
	{
		Debug.Log ("Quitting");
		ReceivedThread.Abort ();
	}
}
